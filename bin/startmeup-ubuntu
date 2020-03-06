#!/bin/bash

qwhich() {
    which $1 > /dev/null
}

apt_it() {
    sudo apt-get -qy --fix-missing install "$@"
}

qwhich docker || apt_it docker.io
qwhich docker-compose || apt_it docker-compose
if groups | grep -q docker; then
    :
else
    sudo usermod -a -G docker uriel
    echo "
Group membership in Linux does not normally take effect immediately.
I'm running 'newgrp - docker'.
This can mess with your RVM and other environment managers.

If Jammer Backend containers don't spin up anyway, you might have to
manually start docker service.
    "
    newgrp - docker
fi
docker-compose up

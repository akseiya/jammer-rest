# Jammer Backend (RESTful with [Eve][eve])

This is the seed and prototype of REST-ful backend for Jammer.

This is an [Eve][eve] app using a standard image for Mongo container
and mutated offspring of [Alex Pankov's Eve Dockerfile][alexdock] for
API box.

[eve]: http://docs.python-eve.org/en/latest/index.html
[alexdock]: https://github.com/alekspankov/docker-eve-python

# Prerequisites

- [Docker](https://docs.docker.com/) 
- [Docker Compose](https://docs.docker.com/compose/)

Both can be installed on Ubuntu by the included
[startmeup script](./bin/startmeup-ubuntu).

Sadly, if you were not previously a member of the `docker` group, there will be unavoidable pain cause by how credentials are propagated in Ubuntu.

If you're not on Ubuntu, you have WSL or some other bad things happen,
check [special cases](#special).

# RUN

The repo includes **docker-compose.yml**. To use it run:

```bash
docker-compose up
```

You can `curl http://0.0.0.0:5000/tadek` as soon as containers are started.
App code volume is mounted live to the container and the app is run with 
`gunicorn --max-requests=1` so that each manual debugging request reloads code.

## toot.py

[`toot`](./bin/toot.py) is a Python minitool for calling the API with
input and output data specified in YAML.

Input data for `POST` and `PUT` requests is read from `stdin`
(press Ctrl+D in empty line to finish)

This toy requires `requests` and `yaml` packages in Python 3 versions (`pip3`).

#### Usage:

```
./bin/toot.py [POST|PUT|DELETE] PATH
```

## durl

[`durl`](./bin/durl) is a little wrapper for curl, preset to go to
`http://0.0.0.0:5000` and to send response to `json_pp`.
- Main parameter is the path.
- It can be followed by JSON data (remember to use quotes!) for POST and PUT
- It can be preceded by 'put' or 'del' to send a PUT/DELETE request.

#### Usage:

```
./bin/durl [put|delete] PATH [DATA]
```

# Changing dependencies

If you modify [dependencies](./requirements.txt), you need to rebuild the images:

```
make
```

```
make build
```

Default target builds the dev container as `akseiya/jammer-backend-dev`
with [dev dockerfile](./docker/Dockerfile.dev),as expected by the 
[docker-compose.yml](./docker-compose.yml).

`build` target only needs to be run for deployments.

<a name="special"></a>

# Everyone is a bit special

## I'm on WSL, please help!

You'll need Docker Desktop for Windows 10 and make it a remote docker server for your WSL. [Nick Janetakis knows how][nickdock].

[nickdock]: https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly

## No can tainer!

You then need to:
- make sure you have Python 3.8 and its very own PIP;
- install dependencies with the right PIP;
- point `python` to Python 3.8;
- run Mongo standalone listening where Eve expects it;
- run `gunicorn --max-requests=1 -b 0.0.0.0:5000 app.app:app` from repo root;
- pray.


# "Production" image, performs a copy of source
# into the container when it's built

FROM python:3.8
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="Jammer back-end" \
    org.label-schema.description="Docker image for seed of Jammer's backend" \
    org.label-schema.url="https://github.com/akseiya/jammer-backend" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/akseiya/jammer-backend" \
    org.label-schema.vendor="Wonsze" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"
LABEL maintainer="Wonsze"

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/* ./

CMD ["gunicorn", "-b 0.0.0.0:5000", "app.app:app"]


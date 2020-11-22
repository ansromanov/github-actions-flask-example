FROM python:3.9-alpine

LABEL org.opencontainers.image.source https://github.com/ansromanov/github-actions-flask-example

RUN apk update
COPY setup.py app/setup.py
COPY requirements.txt app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY app /app/app
RUN pip install -e /app

EXPOSE 8080

ENTRYPOINT [ "simple-web-app" ]
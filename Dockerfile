FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt /requirement.txt


RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
    postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /requirement.txt
RUN apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

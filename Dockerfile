FROM python:3.7-alpine
MAINTAINER nokenku.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /core
WORKDIR /core
COPY ./core /core

RUN adduser -D user
USER user
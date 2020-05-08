FROM ubuntu:18.04
FROM python:3
FROM node:8

MAINTAINER SeongHyukJang "seonghyuk578@khu.ac.kr"

ADD . /Docker

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get install -y curl

CMD [ "/bin/bash" ]
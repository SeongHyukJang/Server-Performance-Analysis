FROM ubuntu:18.04

MAINTAINER SeongHyukJang "seonghyuk578@khu.ac.kr"

ADD . /app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r app/requirements.txt
RUN apt-get install -y curl
RUN apt-get install -y nodejs
RUN apt-get install -y npm

ENV PYTHON_VERSION=3.6.9

ENTRYPOINT [ "/bin/bash" ]
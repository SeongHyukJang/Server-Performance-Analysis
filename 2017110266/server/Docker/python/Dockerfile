FROM ubuntu:18.04

ADD . /app

RUN apt-get update
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

EXPOSE 8000
WORKDIR /app
CMD ["python3", "server.py"]
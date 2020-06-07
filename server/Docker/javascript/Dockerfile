FROM ubuntu:18.04

ADD . /app
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN npm install superagent

EXPOSE 8080
WORKDIR /app
CMD ["node", "server.js"]
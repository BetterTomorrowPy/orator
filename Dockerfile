# Orator`s dockerfile.
# MAINTAINER GuppyGao, 13540171106@163.com

FROM python:latest
MAINTAINER GuppyGao, 13540171106@163.com
WORKDIR /app

RUN mkdir -p /data/logs
RUN mkdir -p /static

# RUN apt-get install apt-transport-https -y

ADD . /app

RUN cp conf/sources.list /etc/apt/sources.list
RUN pip install tornado
RUN apt-get update
# RUN apt-get install nginx -y
RUN apt-get install supervisor -y

# RUN cp ./conf/nginx.conf /etc/nginx/nginx.conf
RUN cp ./conf/supervisord.conf /etc/supervisor/supervisord.conf

VOLUME ["/data"]

EXPOSE 8000 8000

CMD ["/usr/bin/supervisord"]

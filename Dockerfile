# Orator`s dockerfile.
# MAINTAINER GuppyGao, 13540171106@163.com

FROM python:latest
MAINTAINER GuppyGao, 13540171106@163.com
WORKDIR /app

RUN mkdir -p /data/logs

# RUN apt-get install apt-transport-https -y

ADD . /app

RUN cp conf/sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install nginx -y
RUN apt-get install supervisor -y

# RUN cp ./conf/nginx.conf /etc/nginx/nginx.conf
# RUN cp ./conf/supervisord.conf /etc/superisor/supervisorf.conf

VOLUME ["/data"]

EXPOSE 80

CMD ["supervisord", "service nginx restart"]

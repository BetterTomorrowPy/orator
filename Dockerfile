# Orator`s dockerfile.
MAINTAINER Guppy . Gao, 13540171106@163.com

FROM python:latest

WORKDIR /app

RUN mkdir -p /data/logs


ADD ./app
RUN cp ./conf/sources.list /etc/apt/sources.list
RUN apt-get update & apt_get install nginx -y & apt-get install supervisor -y

# RUN cp ./conf/nginx.conf /etc/nginx/nginx.conf
# RUN cp ./conf/supervisord.conf /etc/superisor/supervisorf.conf

VOLUME ['/data']

EXPOSE 80

CMD ['supervisord', 'service nginx restart']
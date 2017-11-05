# nginx-gunicorn-flask

FROM ubuntu:16.04
MAINTAINER CandyBudget Team

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip python-virtualenv nginx supervisor

# Install requirements
COPY requirements.txt /deploy/requirements.txt
RUN pip3 install -r /deploy/requirements.txt

# Mongodb
RUN apt-get install --reinstall -y mongodb
RUN mkdir /data
RUN mkdir /data/db

# Setup db module
RUN mkdir -p /deploy/candy-db
COPY candy-db /deploy/candy-db
RUN cd /deploy/candy-db; python3 setup.py install

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app

# Setup web frontend
RUN mkdir -p /deploy/web
COPY web /deploy/web
COPY run.sh /deploy/run.sh

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
COPY web.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN ln -s /etc/nginx/sites-available/web.conf /etc/nginx/sites-enabled/web.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
#RUN mkdir -p /var/log/supervisor
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#COPY mongod.conf /etc/supervisor/conf.d/mongod.conf
#COPY nginx.conf /etc/supervisor/conf.d/nginx.conf
#RUN ls
#COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Volume
VOLUME /data/db

WORKDIR /deploy/app

# Start processes
CMD ["/bin/bash", "/deploy/run.sh"]

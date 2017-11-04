## nginx-gunicorn-flask-web

This repository contains files necessary for building a Docker image of
Nginx + Gunicorn + Flask + Frontend.


### Base Docker Image

* [ubuntu:16.04](https://registry.hub.docker.com/_/ubuntu/)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Build:
	
```bash
docker build -it candybudget .
```


### Usage

```bash
docker run -it -p 80:80 -p 5000:5000 candybudget
```

After few seconds, open `http://<host>` to see the Flask app.

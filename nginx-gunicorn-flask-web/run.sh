#!/bin/bash

/usr/bin/mongod &
/usr/sbin/nginx &


cd /deploy/app
python3 run.py
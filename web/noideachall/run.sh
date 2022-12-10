#!/bin/bash

docker build -t firstchall --build-arg host=$1 ./webapp
docker run -d --name firstchallweb -p 5000:5000 firstchall
docker build -t bot --build-arg host=$1 ./bot
docker run -d --name firstchallbot bot

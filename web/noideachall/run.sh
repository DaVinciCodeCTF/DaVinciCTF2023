#!/bin/bash

docker build -t noidea --build-arg ./webapp
docker run -d --name noidea -p 5000:5000 noidea
docker build -t noidea_bot --build-arg host=$1 ./bot
docker run -d --name noidea_bot noidea_bot

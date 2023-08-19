#!/usr/bin/env sh
docker kill jonny
docker rm jonny
docker-compose build
docker-compose up -d

#!/bin/env sh

socat TCP4-LISTEN:8888,reuseaddr,fork EXEC:'./start.sh',pipes

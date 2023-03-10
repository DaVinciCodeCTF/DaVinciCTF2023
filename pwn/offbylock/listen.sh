#!/bin/env sh

socat TCP4-LISTEN:8888,fork EXEC:'./start.sh',pipes

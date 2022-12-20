FROM alpine

RUN apk update && apk add s6-networking python3.10 py3-pip
RUN adduser carlsen -D
RUN pip3 install stockfish
RUN pip3 install numpy
RUN pip3 install matplotlib

COPY . /ChessChall/
WORKDIR /ChessChall/

USER carlsen
CMD s6-tcpserver 0.0.0.0 6464 python3 ChessProj.py


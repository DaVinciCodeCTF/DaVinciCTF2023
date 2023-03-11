FROM ubuntu@sha256:b2175cd4cfdd5cdb1740b0e6ec6bbb4ea4892801c0ad5101a81f694152b6c559 AS app

RUN apt-get update 
RUN apt-get install -y build-essential socat binutils-x86-64-linux-gnu
RUN rm -rf /var/lib/apt/lists/*

COPY run /app/run
COPY lvl1.c /app/lvl1.c
COPY lvl2.c /app/lvl2.c
COPY lvl3.c /app/lvl3.c
COPY seccomp-bpf.h /app/seccomp-bpf.h
# RUN cp /srv/bin/bash /srv/app/run
WORKDIR /app/
EXPOSE 5000

CMD ["sh", "-c", "socat TCP-LISTEN:5000,reuseaddr,fork EXEC:'timeout 60 ./run',stderr,pty,echo=0", ""]

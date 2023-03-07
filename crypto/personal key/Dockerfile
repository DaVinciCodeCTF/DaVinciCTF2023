FROM alpine:latest

ENV TIMEZONE Europe/Paris 
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/* 
RUN apk update && apk add --no-cache socat python3 py3-pip gcc g++ make libffi-dev openssl-dev python3-dev build-base --update-cache 

COPY script.py /challenge/script.py

RUN addgroup --gid 1000 challenge && \ 
        adduser --uid 1000 --disabled-password --home=/challenge --ingroup challenge challenge 

RUN python3 -m pip install pycryptodome 

WORKDIR /challenge/ 

RUN chown challenge:challenge /challenge/script.py && chmod +x /challenge/script.py 

USER 1000 

EXPOSE 2000 

CMD ["sh", "-c", "socat TCP-LISTEN:2000,reuseaddr,fork EXEC:'python3 /challenge/script.py',stderr,pty,echo=0", ""]
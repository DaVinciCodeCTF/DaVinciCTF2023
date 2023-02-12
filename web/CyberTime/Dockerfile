FROM alpine

RUN apk update && apk upgrade
RUN apk add python3
RUN python3 -m ensurepip --default-pip

WORKDIR /app/

ADD . ./cybertime/

WORKDIR ./cybertime/

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

ARG host
ENV HOST=$host

CMD ["python3", "./app.py"]
FROM alpine

RUN apk update && apk upgrade
RUN apk add python3
RUN python3 -m ensurepip --default-pip

WORKDIR /home/app/

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "./app.py"]

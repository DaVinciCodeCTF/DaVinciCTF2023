docker build -t cybertime --build-arg host=$1 .
docker run --restart=always --name cybertime -d -p 8088:5000 cybertime
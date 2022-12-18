docker build -t astro1 ./webapp
docker run --restart=always --name astro1 -d -p 8085:8085 astro1
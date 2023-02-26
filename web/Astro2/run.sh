docker build -t astro2 ./webapp
docker run --restart=always --name astro2 -d -p 8086:8086 astro2
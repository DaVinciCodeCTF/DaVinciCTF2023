docker build -t astro_web_chall ./webapp
docker run --restart=always --name astro_chall -d -p 8085:8085 astro_web_chall
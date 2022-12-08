docker build -t astro2_web_chall ./webapp
docker run --restart=always --name astro2_chall -d -p 8086:8086 astro2_web_chall
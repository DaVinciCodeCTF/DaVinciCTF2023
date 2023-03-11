docker build -t astro3 ./webapp
docker run --restart=always --name astro3 -d -p 8087:8087 astro3
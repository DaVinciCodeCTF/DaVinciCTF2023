FROM node:latest

WORKDIR /tmp
RUN curl -Lo "deno.zip" "https://github.com/denoland/deno/releases/download/v1.28.2/deno-x86_64-unknown-linux-gnu.zip"
RUN unzip -d /usr/local/bin /tmp/deno.zip

WORKDIR /app/
ADD . ./astro_web_chall/
WORKDIR ./astro_web_chall/

RUN npm ci
RUN npm run build

EXPOSE 8087

CMD npm run preview
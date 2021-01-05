FROM alpine:latest

EXPOSE 4200

WORKDIR /root

RUN apk update && \
    apk upgrade && \
    apk add --no-cache git bash nodejs npm && \
    npm install -g @angular/cli && \
    git clone https://github.com/tuimac/serverless_sample.git

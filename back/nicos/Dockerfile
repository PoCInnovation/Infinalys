FROM alpine:latest

WORKDIR /app

COPY package.json /app

COPY . /app

RUN apk add --update nodejs npm
RUN npm install -g express

CMD [ "node", "index.js" ]

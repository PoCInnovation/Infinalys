FROM alpine:latest

WORKDIR /app

COPY . /app
# RUN sysctl fs.inotify.max_user_watches=16000
RUN apk add --update nodejs npm
RUN npm install

ENV PORT=4444

CMD [ "npm", "start" ]

FROM node:latest

WORKDIR /app

COPY package.json /app

RUN npm install
# RUN sysctl fs.inotify.max_user_watches=16000

COPY . /app

ENV PORT=4444

CMD [ "npm", "start" ]
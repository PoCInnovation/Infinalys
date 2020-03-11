FROM node:latest

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

ENV PORT=4444

CMD [ "npm", "start" ]
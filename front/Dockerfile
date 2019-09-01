# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app/frontend/

# add `/app/frontend/node_modules/.bin` to $PATH
ENV PATH /app/frontend/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/frontend/package.json
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent

EXPOSE 80

# start app
CMD ["npm", "start"]

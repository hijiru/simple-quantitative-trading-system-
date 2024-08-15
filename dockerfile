
  GNU nano 8.0        dockerfile                  FROM node:14 as base
FORM node:20-alpine

WORKDIR /home/node/app

COPY package.json ./

COPY tsconfig ./

RUN npm i

COPY . .

RUN npm start

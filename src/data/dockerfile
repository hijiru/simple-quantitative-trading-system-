
FROM node:20-alpine

WORKDIR /home/node/app

COPY package.json ./

COPY tsconfig.json ./

RUN npm i

COPY . .

CMD ["npm","start"]

FROM node:18-alpine

WORKDIR /react-vite-app

COPY package.json package-lock.json ./

RUN npm install --legacy-peer-deps

COPY . ./

CMD ["npm", "start"]
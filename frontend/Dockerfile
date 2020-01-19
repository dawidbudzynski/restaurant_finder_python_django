FROM node:12.2.0-alpine

WORKDIR /app/

COPY package.json package.json
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent

COPY . /app/

EXPOSE 3000

CMD npm start
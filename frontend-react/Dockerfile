FROM stefanscherer/node-windows:12.18.3-windowsservercore-2019

WORKDIR C:\\frontend-react

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
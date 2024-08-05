FROM mcr.microsoft.com/windows/servercore:ltsc2019

ENV NODE_VERSION=20.16.0

WORKDIR C:\\frontend-react

COPY add_node_in_path.ps1 .

# Download Node.js installer
RUN powershell -Command Invoke-WebRequest -Uri "https://nodejs.org/dist/v%NODE_VERSION%/node-v%NODE_VERSION%-win-x64.zip" -OutFile node.zip;

# Unzip the installer
RUN powershell -Command Expand-Archive node.zip -DestinationPath C:\;
    
# Remove the downloaded zip file
RUN powershell -Command Remove-Item node.zip;

# Rename the extracted folder
RUN powershell -Command Rename-Item "C:\node-v%NODE_VERSION%-win-x64" "C:\nodejs";

RUN powershell -Command Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine

RUN powershell -NoProfile -File ./add_node_in_path.ps1

# Verify Node.js installation 
RUN node --version && npm --version

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

# Set the entry point (optional)
ENTRYPOINT ["powershell.exe"]

CMD ["npm", "start"]
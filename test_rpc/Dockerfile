# node:alpine will be our base image to create this image
FROM node:16
# Set the /app directory as working directory
WORKDIR /app
# Install ganache-cli globally
RUN npm install -g ganache-cli
# Set the default command for the image
CMD ["ganache-cli", "-m", "fruit mind injury stadium voice rebel arrange horn area pulp chair tiny", "-h", "0.0.0.0"]

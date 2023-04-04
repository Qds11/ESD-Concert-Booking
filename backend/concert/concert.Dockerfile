# Specify a base image
FROM node:14-alpine

# Set the working directory
WORKDIR /usr/src/app

COPY ./app.js .
# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY config.js ./
COPY db.js ./
COPY model.js ./
COPY node_modules ./


# Expose the port that the app will listen on
EXPOSE 5005

# Start the application
CMD ["node", "./app.js"]

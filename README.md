# TicketPRO

## Introduction
This is a web application that simulates the purchasing of concert tickets. Users can view available concerts and choose to purchase tickets for them. If there are too many people currently purchasing tickets, they will be held in a virtual queue and redirected to continue the ticketing process (including seat selection and payment) when it's their turn.

To provide these features, this web application uses several external APIs, including Google Authentication for user login, Twilio for sending SMS notifications on payment and queue status, and PayPal for payment processing. In addition, an AMQP (Advanced Message Queuing Protocol) service is implemented for the queue, allowing messages to be published to a notification service for sending SMS notifications to users.

To protect sensitive user data such as email addresses and phone numbers, an API gateway is implemented for the user microservice.

Finally, this web application is designed to be containerized using Docker into individual microservices, enabling better scalability, flexibility, and maintainability. 

## Requirements
1) Have Docker installed in your host system

3) A compatible host operating system that supports Docker, such as Linux, macOS, or Windows.

2) Sufficient resources on the host system to run the container, including CPU, RAM, and storage.

3) A network connection to access the container registry and to communicate with the web application.

4. Any required environment variables such as API keys or credentials to configure the web application. These can be passed to the container using the -e option when running docker run.

## Project setup
1) Clone the GitHub repository using the git clone command.

2) Navigate to the directory containing the docker-compose.yml file.

3) Run the docker-compose up command to start all services defined in the docker-compose.yml file.

4) Access the web application by navigating to the container's IP address or hostname on the specified port.

5) npm install in root directory

6) npm run dev in root directory to start up frontend  
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



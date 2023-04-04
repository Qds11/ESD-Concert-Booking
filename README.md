# TicketPRO

## Introduction
This is a web application that simulates the purchasing of concert tickets. Users can view available concerts and choose to purchase tickets for them. If there are too many people currently purchasing tickets, they will be held in a virtual queue and redirected to continue the ticketing process (including seat selection and payment) when it's their turn.

To provide these features, this web application uses several external APIs, including Google Authentication for user login, Twilio for sending SMS notifications on payment and queue status, and PayPal for payment processing. In addition, an AMQP (Advanced Message Queuing Protocol) service is implemented for the queue, allowing messages to be published to a notification service for sending SMS notifications to users.

To protect sensitive user data such as email addresses and phone numbers, an API gateway is implemented for the user microservice.

Finally, this web application is designed to be containerized using Docker into individual microservices, enabling better scalability, flexibility, and maintainability. 

## Project setup
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



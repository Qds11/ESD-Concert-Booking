# TicketPRO

## Introduction
This is a web application that simulates the purchasing of concert tickets. Users can view available concerts and choose to purchase tickets for them. If there are too many people currently purchasing tickets, they will be held in a virtual queue. Once the user is at the front of the queue, they will be directed to select seats where recommended seats will be provided based on user's historical seat preferences (if user is logged in) and then directed to payment to complete the ticket purchasing process. 

To provide these features, this web application uses several external APIs, including Google Authentication for user login, Twilio for sending SMS notifications on payment and queue status, and PayPal for payment processing. In addition, an AMQP (Advanced Message Queuing Protocol) service is implemented for the queue, allowing messages to be published to a notification service for sending SMS notifications to users.

To protect sensitive user data such as email addresses and phone numbers, an API gateway is implemented for the user microservice.

Finally, this web application is designed to be containerized using Docker into individual microservices, enabling better scalability, flexibility, and maintainability. 

## Requirements
1) Have Docker and Docker Compose installed in your host system.

2) A compatible host operating system that supports Docker, such as Linux, macOS, or Windows.

3) Sufficient resources on the host system to run the container, including CPU, RAM, and storage.

4) A network connection to access the container registry and to communicate with the web application.

5) Any required environment variables such as API keys or credentials to configure the web application. These can be passed to the container using the -e option when running docker run.

## Project setup
1) Clone the GitHub repository using the git clone command.

2) Navigate to the directory containing the docker-compose.yml file.

3) Run the docker-compose up command to start all services defined in the docker-compose.yml file.

4) Access the web application by navigating to the container's IP address or hostname on the specified port.

5) Install dependencies in root directory:
```
npm install
```
6) Start up the frontend by running the following command in the root directory:  
```
npm run serve
```

## Web Application Flow

  1) Users can choose to log in using google authentication or can directly go to the homepage
  
![image](https://user-images.githubusercontent.com/101784318/229842130-6062a318-b7cc-48f4-b6f8-f671165fc7b6.png)

  ![image](https://user-images.githubusercontent.com/101784318/229825589-da735d46-56a2-4a7f-9189-4d7e1e887d39.png)


  3) Homepage will display list of concerts with recommended concert based on user preferred genre
 ![image](https://user-images.githubusercontent.com/101784318/229833012-35a40378-0e01-4b13-bf58-6d1ad55ba01e.png)

  4) If user clicks 'Explore' for a specific concert, they will be directed to this page where they can purchase the tickets if tickets are still available and ticket sales are open
  ![image](https://user-images.githubusercontent.com/101784318/229832715-d59fafa9-2c29-4561-bec5-eabc8d8c7f48.png)

  5) Once user clicks on 'Buy Tickets' button, they will be directed to the virtual queue page where if there are 4 or more other users currently purchasing tickets for the same concert, they will have to wait for their turn. 
  ![image](https://user-images.githubusercontent.com/101784318/229836742-c5aae28b-75f0-4727-a429-77ef66566775.png)


  6) If user is at queue position 4, they will receive an SMS that notifies them that they are nearing the front of the queue.
  ![image](https://user-images.githubusercontent.com/101784318/229839124-d5d564f5-fba9-448d-af37-e137a0908c84.png)

  7) Once they are at queue position 0, they will be directed to seat selection page. They have a total of 10 minutes to complete selecting seats and payment.
![image](https://user-images.githubusercontent.com/101784318/229840198-64348466-8a71-4e28-8cb9-b0a32a2ca7b2.png)


  
  8) If they try to checkout with more than 10 tickets or if the tickets are sold out, they will be notified and cannot proceed to payment.
  ![image](https://user-images.githubusercontent.com/101784318/229839678-3c0f712f-bebd-47de-9fd0-06c82eab9682.png)

  
  9) At checkout, they will be directed to payment page where paypal is used.
  ![image](https://user-images.githubusercontent.com/101784318/229840933-03a06132-c4b0-43da-a94f-1181415713af.png)
  ![image](https://user-images.githubusercontent.com/101784318/229841177-ab41618d-abfd-4f52-bc5a-7eb6229ec219.png)


  10) If payment is successful, they will receive a payment success notification through SMS
  





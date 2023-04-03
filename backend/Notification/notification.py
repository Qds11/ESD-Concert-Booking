from flask import Flask, jsonify
from flask_cors import CORS

import os
import requests
from invokes import invoke_http
import twilio

from twilio.rest import Client

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

# Download the helper library from https://www.twilio.com/docs/python/install

# Set environment variables for your credentials
# Read more at http://twil.io/secure

user_URL = "http://127.0.0.1:5000/user/phoneNum/"


# get phone num frm user id and find the user phone number
@app.route('/sendQueueNotification/<string:user_id>', methods=['GET'])
def send_notif_queue(user_id):

    result = invoke_http(user_URL + user_id, method='GET')
    code = result['code']
    phone_num = result['phone_num']

    # Your Account SID from twilio.com/console
    account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
    # Your Auth Token from twilio.com/console
    auth_token = "72769e6ae2bb619d91fd600733634fbb"
    # code = 500

    client = Client(account_sid, auth_token)
    if code not in range(200, 300):

        message = json.dumps(result)

        amqp_setup.channel.basic_publish(
            exchange=amqp_setup.exchangename,
            routing_key="queue.error_notif",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2))

        return jsonify({"code": 404, "message": "message not sent"}), 404

    message = client.messages.create(
        to="+65" + str(phone_num),
        from_="+15178269570",
        body=
        "You are currently 3 places away from the Seat Selection Page! \n Do take note that you will have 10 mins to select your seats after entering!"
    )

    return jsonify({"code": 200, "message": "Notification is sent"})


# get phone num frm user queue and find the user phone number
@app.route('/sendPaymentNotification/<string:user_id>', methods=['GET'])
def send_payment_queue(user_id):

    result = invoke_http("http://127.0.0.1:5000/user/phoneNum/" + user_id,
                         method='GET')

    code = result['code']
    phone_num = result['data']

    # Your Account SID from twilio.com/console
    account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
    # Your Auth Token from twilio.com/console
    auth_token = "72769e6ae2bb619d91fd600733634fbb"

    client = Client(account_sid, auth_token)
    if code not in range(200, 300):

        message = json.dumps(result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename,
        routing_key="payment.error_notif",
        body=message,
        properties=pika.BasicProperties(delivery_mode=2))

        return jsonify({"code": 404, "message": "message not sent"}), 404


    message = client.messages.create(
        to="+65" + str(phone_num),
        from_="+15178269570",
        body=
        "You have purchased the ticket successfully!"
    )

    return jsonify({"code": 200, "message": "notification is sent"})


if __name__ == '__main__':
    print("This is flask " + os.path.basename(__file__) +
          " for sending a notification...")
    app.run(debug=True, port=5100)

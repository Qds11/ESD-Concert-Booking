from flask import Flask, jsonify
# from flask_cors import CORS
from twilio.rest import Client
import os
import requests
import json
from invokes import invoke_http
import pika 
import sys

monitorBindingKey='*.notif'

# app = Flask(__name__)
# CORS(app)

user_URL="http://localhost:8000/api/v1/user/phoneNum/" + user_id + "?apikey=QRp2hItGLsgHXWD0CHVGBSHxJB6wEO7i"

# Twilio account credentials
TWILIO_ACCOUNT_SID = "ACb73a42a689c04ad6bf175a645cfa9282"
TWILIO_AUTH_TOKEN = "72769e6ae2bb619d91fd600733634fbb"
TWILIO_PHONE_NUMBER = "+15178269570"

# send payment notification to user
# @app.route('/sendPaymentNotification/<string:user_id>', methods=['GET'])
# def send_payment_notification(user_id):
#     try:
#         result = invoke_http(user_url + user_id, method='GET')
#         code = result['code']
#         phone_num = result['data']

#         client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#         message = client.messages.create(
#             to="+65" + str(phone_num),
#             from_=TWILIO_PHONE_NUMBER,
#             body="You have purchased the ticket successfully"
#         )
#     except Exception as e:
#         return jsonify({"code": 500, "message": "Failed to send notification: " + str(e)})

def recieveQueue():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='notif_topic', exchange_type='topic')
    
    queue_name = "Notification"

    channel.queue_declare(queue_name, durable=True)

    queue_name = "Notification"

    binding_key = "*.notif"

    channel.queue_bind(exchange='notif_topic', queue=queue_name, routing_key=binding_key)

    channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

    print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an notification requrest by " + __file__)

    send_notif_queue(json.loads(body))
    print() # print a new line feed
 
# send user reminder when they are 3 places away from the seat selection page
def send_notif_queue(user_id):
        print("inside send_notif_queue")
    # try:
        result = invoke_http(user_url + str(user_id), method='GET')
        phone_num = result['data']

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
                to="+65" + str(phone_num),
                from_=TWILIO_PHONE_NUMBER,
                body="You are currently 3 places away from the Seat Selection Page!"
                     "\nDo take note that you will have 10 mins to select your seats after entering!"
        )
        print(message.sid)


if __name__ == '__main__':
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, "notif_topic"))

    recieveQueue()


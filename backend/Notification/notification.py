from flask import Flask, jsonify
import os
import twilio
import requests
from invokes import invoke_http
from twilio.rest import Client

app = Flask(__name__)

# Download the helper library from https://www.twilio.com/docs/python/install

# Set environment variables for your credentials
# Read more at http://twil.io/secure


@app.route('/testing')
def testing():
    # Your Account SID from twilio.com/console
    account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
    # Your Auth Token from twilio.com/console
    auth_token = "72769e6ae2bb619d91fd600733634fbb"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+65" + "90628232",
        from_="+15178269570",
        body="Congrats your purchase has been confirmed!")

    print(message.sid)
    return message


# get phone num frm user queue and find the user phone number
@app.route('/sendQueueNotification/<string:user_id>', methods=['GET'])
def send_notif_queue(user_id):

    phone_num = invoke_http("http://127.0.0.1:5000/user/phoneNum//" + user_id,
                            method='GET')

    # Your Account SID from twilio.com/console
    account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
    # Your Auth Token from twilio.com/console
    auth_token = "72769e6ae2bb619d91fd600733634fbb"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+65" + {phone_num},
        from_="+15178269570",
        body=
        "You are currently 3 places away from the Seat Selection Page! \n Do take note that you will have 10 mins to select your seats after entering!"
    )
    if (message):
        return jsonify({"code": 200, "message": message.sid})
    else:
        return jsonify({"code": 404, "message": "message not sent"}), 404


# get phone num frm user queue and find the user phone number
@app.route('/sendPaymentNotification/<string:user_id>', methods=['GET'])
def send_payment_queue(user_id):

    phone_num = invoke_http("http://127.0.0.1:5000/user/phoneNum//" + user_id,
                            method='GET')

    # Your Account SID from twilio.com/console
    account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
    # Your Auth Token from twilio.com/console
    auth_token = "72769e6ae2bb619d91fd600733634fbb"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+65" + {phone_num},
        from_="+15178269570",
        body=
        "You are currently 3 places away from the Seat Selection Page! \n Do take note that you will have 10 mins to select your seats after entering!"
    )

    if (message):
        return jsonify({"code": 200, "message": message.sid})
    else:
        return jsonify({"code": 404, "message": "message not sent"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5100)

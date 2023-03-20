from flask import Flask
import os
import twilio
from twilio.rest import Client


app = Flask(__name__)

# Download the helper library from https://www.twilio.com/docs/python/install

# Set environment variables for your credentials
# Read more at http://twil.io/secure

# get phone num frm user
@app.route('/sendNotification')
def send_notif(phone_num):
# call user here?
   # Your Account SID from twilio.com/console
   account_sid = "ACb73a42a689c04ad6bf175a645cfa9282"
   # Your Auth Token from twilio.com/console
   auth_token  = "72769e6ae2bb619d91fd600733634fbb"

   client = Client(account_sid, auth_token)

   message = client.messages.create(
      to="+65" + {phone_num}, 
      from_="+15178269570",
      body="Hello from Python!")

   print(message.sid)

if __name__ == '__main__':
   app.run(debug = True)
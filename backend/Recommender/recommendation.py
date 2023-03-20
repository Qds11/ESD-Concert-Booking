from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date
import requests
from invokes import invoke_http
app = Flask(__name__)

# #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# # for local db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/ticket_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




CORS(app)





#api endpoint for concert ms to call, will call user ms and return the result from user to concert
@app.route("/user/<string:user_id>")
def find_genre_by_calling_user(user_id):
    results = invoke_http("http://127.0.0.1:5000/user/"+user_id, method='GET')
    if results['code']==200:
        return jsonify(
        {
            "code": 200,
            "message": results['message']
        }
    ), 200
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404


#part2 talking to ticketing to retrieve seating availability and recommend, retrieve user birthdate and recommend 

results = invoke_http("http://127.0.0.1:5000/user/birthday/1", method='GET')

birthdate=results['message']


# convert to datetime object
date_obj = datetime.strptime(birthdate, "%a, %d %b %Y %H:%M:%S %Z")

# format the datetime object to desired format
formatted_date = date_obj.strftime("%d/%m/%Y")

# convert to datetime object
date_obj = datetime.strptime(formatted_date, "%d/%m/%Y")

# calculate age
age = (date.today() - date_obj.date()).days // 365

#part2 talking to



results = invoke_http("http://127.0.0.1:5000/avail/", method='GET')
    
    







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

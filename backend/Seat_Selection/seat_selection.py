from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date
import requests
from invokes import invoke_http

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# for local db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/seat_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

@app.route("/reserve-seats/<string:concert_id>/<int:num_seats>", methods=['POST'])
def reserve_seats(concert_id, num_seats):
    # Get available seats for the concert from the ticketing microservice
    seat_results = invoke_http("http://127.0.0.1:5004/" + str(num_seats), method='GET')

    # Check if there are any available seats
    if seat_results["code"] == 200 and len(seat_results["seats"]) >= num_seats:
        # If there are available seats, select the first 'num_seats' seats
        selected_seats = seat_results["seats"][:num_seats]

        # Reserve the selected seats
        reservation_results = invoke_http("http://127.0.0.1:5004/reserve-seats/" + concert_id, method='POST', json={
            "seats": selected_seats
        })

        # Check if the reservation was successful
        if reservation_results["code"] == 200:
            # If the reservation was successful, return the selected seats as a list
            return jsonify({
                "code": 200,
                "seats": selected_seats
            }), 200
        else:
            # If the reservation was not successful, return an error message
            return jsonify({
                "code": 500,
                "message": "Seat reservation failed"
            }), 500
    else:
        # If there are no available seats, return an error message
        return jsonify({
            "code": 404,
            "message": "No available seats"
        }), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)

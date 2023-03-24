from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TICKETING_MICROSERVICE_URL = "http://localhost:5004"

# get available seats for a concert
@app.route('/seats', methods=['GET'])
def get_available_seats():
    concert_id = request.args.get('concert_id')
    response = requests.get(f"{TICKETING_MICROSERVICE_URL}/avail/{concert_id}")
    if response.status_code == 200:
        availability = response.json()
        return jsonify(availability)
    return jsonify({"error": "Unable to get availability"}), 500

# reserve seats for a concert
@app.route('/reserve', methods=['POST'])
def reserve_seats():
    concert_id = request.json.get('concert_id')
    seat_type = request.json.get('seat_type')
    num_seats = request.json.get('num_seats')

    # get the hall ID for the concert
    hall_response = requests.get(f"{TICKETING_MICROSERVICE_URL}/hall/{concert_id}")
    if hall_response.status_code != 200:
        return jsonify({"error": "Unable to get hall information"}), 500
    hall_id = hall_response.json().get('data')

    # get the price for the seat type
    price_response = requests.get(f"{TICKETING_MICROSERVICE_URL}/price/{concert_id}")
    if price_response.status_code != 200:
        return jsonify({"error": "Unable to get price information"}), 500
    price = price_response.json().get(f"{seat_type}_price")

    # reserve the seats
    reservation_data = {
        "hall_id": hall_id,
        "concert_id": concert_id,
        "seat_type": seat_type,
        "num_seats": num_seats,
        "price": price
    }
    response = requests.post("http://localhost:5005/reserve", json=reservation_data)
    if response.status_code == 200:
        reservation_id = response.json().get('reservation_id')
        return jsonify({"reservation_id": reservation_id})
    return jsonify({"error": "Unable to reserve seats"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)

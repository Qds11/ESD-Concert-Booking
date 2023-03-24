from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Seat(db.Model):
    __tablename__ = 'seats'

    id = db.Column(db.Integer, primary_key=True)
    hall_id = db.Column(db.Integer, nullable=False)
    seat_count = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    seatnumber = db.Column(db.String(64), nullable=False)

    def __init__(self, hall_id, seat_count, category, seatnumber):
        self.hall_id = hall_id
        self.seat_count = seat_count
        self.category = category
        self.seatnumber = seatnumber

    def json(self):
        return {"id": self.id, "hall_id": self.hall_id, "seat_count": self.seat_count, "category": self.category, "seatnumber": self.seatnumber}

@app.route("/seats")
def get_all_seats():
    seats = Seat.query.all()
    if len(seats):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "seats": [seat.json() for seat in seats]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no seats."
        }
    ), 404

@app.route("/seats", methods=['POST'])
def add_seat():
    data = request.get_json()
    seat = Seat(hall_id=data['hall_id'], seat_count=data['seat_count'], category=data['category'], seatnumber=data['seatnumber'])
    try:
        db.session.add(seat)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the seat."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": seat.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
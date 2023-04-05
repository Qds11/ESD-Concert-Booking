from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import json
import requests
from invokes import invoke_http
import pika
import sys
from os import environ


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# for local db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/queue_database'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/concertdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

CORS(app)


class Concert(db.Model):
   concert_id = db.Column(db.Integer, primary_key=True)
   date_time = db.Column(db.DateTime, nullable=False)
   ticket_sale_date_time = db.Column(db.DateTime, nullable=False)
   artist = db.Column(db.Text, nullable=False)
   concert_name = db.Column(db.Text, nullable=False)
   description = db.Column(db.Text, nullable=False)
   image_path = db.Column(db.Text, nullable=False)
   genre = db.Column(db.Text, nullable=False)
   price = db.Column(db.Integer, nullable=False)
   status = db.Column(db.Integer, nullable=False)
   hall_id = db.Column(db.Integer, nullable=False)

   def json(self):
        return {
            'concert_id': self.concert_id,
            'date_time': self.date_time.isoformat(),
            'ticket_sale_date_time': self.ticket_sale_date_time.isoformat(),
            'artist': self.artist,
            'concert_name': self.concert_name,
            'description': self.description,
            'image_path': self.image_path,
            'genre': self.genre,
            'price': self.price,
            'status': self.status,
            'hall_id': self.hall_id,
        }


###### queue ui call this once to queue user regardless whether they actually need to queue####
@app.route('/', methods=['GET'])
def get_concert_details():
    try:
        # Check the number of rows with the status 'serving' (add seat selection page)
      concerts = Concert.query.all()
      userId = request.args.get('userId')
      #userId=data['userId']
      if userId:
        results=invoke_http("http://127.0.0.1:5003/recommendations/user/"+str(userId), method='GET')
        print(results)
        genre=results['message']
      else:
          genre=None

      if len(concerts):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "concerts": [concert.json() for concert in concerts],
                     "recommended": genre
                }
            }
        )
      return jsonify(
        {
            "code": 404,
            "message": "There are no concerts."
        }
      ), 404
    except Exception as e:
        return jsonify({
            'code':
            500,
            'message':
            "Error occurred when getting concerts: " + str(e)
        }), 500

##### queue iu freqeuently call this to updated queue position #####
@app.route('/concert/<int:id>')
def get_concert_by_id(id):
    try:
        concert = Concert.query.filter_by(concert_id=id).first()
        if concert is None:
            return jsonify({
                'code': 404,
                'message': 'Concert not found'
            }), 404

        if concert.status == 'closed':
            return jsonify({
                "code": 200,
                "data": concert.json()
            }), 200
        if concert.status == 'Concert available':
            try:
                results=invoke_http("http://ticketing:5004/concert/status/"+str(id), method='GET')
                status=results['status']
                if status == 'Concert sold out':
                    concert.status='Concert sold out'
                    db.session.commit()
            except Exception as e:
                return jsonify({
                    'status':
                    'error',
                    'message':
                    "Error occurred when getting concert status: " + str(e)
                }), 500
        try:
            hall_data=invoke_http("http://ticketing:5004/hall/"+str(id), method='GET')
            concert_dict = concert.json()
            concert_dict["hall_name"] = hall_data["hall_name"]
            concert_dict["hall_plan"] = hall_data["hall_plan"]

        except Exception as e:
                return jsonify({
                    'status':
                    'error',
                    'message':
                    "Error occurred when getting hall data: " + str(e)
                }), 500

        return jsonify({
                "code": 200,
                "data": concert_dict
            }), 200

    except Exception as e:
        return jsonify({
            'status':
            'error',
            'message':
            "Error occurred when getting concert by id: " + str(e)
        }), 500


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5005, debug=True)
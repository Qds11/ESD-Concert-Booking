from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
cors = CORS(app)

# need to change DB uri accordingly
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/halldata'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/halldata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Ticket(db.Model):
    __tablename__ = 'hall'


    hall_id = db.Column(db.Integer)
    hall_plan = db.Column(db.String(128), nullable=False)
    hall_name = db.Column(db.String(128), nullable=False)
    concert_id = db.Column(db.Integer, primary_key=True)
    concert_date=db.Column(db.Date, nullable=False)
    cat1_avail=db.Column(db.Integer,nullable=False)
    cat2_avail=db.Column(db.Integer,nullable=True)
    cat3_avail=db.Column(db.Integer,nullable=True)
    cat4_avail=db.Column(db.Integer,nullable=True)
    cat5_avail=db.Column(db.Integer,nullable=True)
    cat1_price=db.Column(db.Integer, nullable=False)
    cat2_price=db.Column(db.Integer, nullable=True)
    cat3_price=db.Column(db.Integer, nullable=True)
    cat4_price=db.Column(db.Integer, nullable=True)
    cat5_price=db.Column(db.Integer, nullable=True)

    def __init__(self, hall_id, hall_plan, hall_name, concert_id, concert_date, cat1_avail, cat2_avail, cat3_avail, cat4_avail, cat5_avail,cat1_price, cat2_price,cat3_price,cat4_price,cat5_price):
        self.hall_id=hall_id
        self.hall_plan=hall_plan
        self.hall_name=hall_name
        self.concert_id=concert_id
        self.concert_date=concert_date
        self.cat1_avail=cat1_avail
        self.cat2_avail=cat2_avail
        self.cat3_avail=cat3_avail
        self.cat4_avail=cat4_avail
        self.cat5_avail=cat5_avail
        self.cat1_price=cat1_price
        self.cat2_price=cat2_price
        self.cat3_price=cat3_price
        self.cat4_price=cat4_price
        self.cat5_price=cat5_price


    def json(self):
        return {"hall_id": self.hall_id, "hall_plan":self.hall_plan, "hall_name":self.hall_name, "concert_id":self.concert_id, "concert_date":self.concert_date, "cat1_avail":self.cat1_avail, "cat2_avail":self.cat2_avail, "cat3_avail":self.cat3_avail, "cat4_avail":self.cat4_avail, "cat5_avail":self.cat5_avail,"cat1_price":self.cat1_price, "cat2_price":self.cat2_price, "cat3_price":self.cat3_price, "cat4_price":self.cat4_price, "cat5_price":self.cat5_price}


cors = CORS(app, resources={r'/*': {'origins': '*'}})


# get availability by providing concert_id
@app.route('/avail/<string:concert_id>', methods=['GET'])
def get_availability(concert_id):
    ticket = Ticket.query.filter_by(concert_id=concert_id).first()
    if ticket:
        return jsonify(
            {
                "code": 200,
                "cat1_avail": ticket.json()['cat1_avail'],
                "cat2_avail": ticket.json()['cat2_avail'],
                "cat3_avail": ticket.json()['cat3_avail'],
                "cat4_avail": ticket.json()['cat4_avail'],
                "cat5_avail": ticket.json()['cat5_avail'],
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no concerts by that concert id."
        }
    ), 404





# get prices by providing concert id 
@app.route('/price/<string:concert_id>', methods=['GET'])
def get_prices(concert_id):
    ticket = Ticket.query.filter_by(concert_id=concert_id).first()
    if ticket:
        return jsonify({
            "code": 200,
            "cat1_price":ticket.json()['cat1_price'],
            "cat2_price":ticket.json()['cat2_price'],
            "cat3_price":ticket.json()['cat3_price'],
            "cat4_price":ticket.json()['cat4_price'],
            "cat5_price":ticket.json()['cat5_price']
        })

    return jsonify(
        {
            "code": 404,
            "message": "There are no concerts by that concert id."
        }
    ), 404

#get hall_id
@app.route('/hall/<string:concert_id>', methods=['GET'])
def get_hall(concert_id):
    ticket = Ticket.query.filter_by(concert_id=concert_id).first()
    if ticket:
        return jsonify({
            "code": 200,
            "data":ticket.json()['hall_id'],
            "hall_plan":ticket.json()['hall_plan'],
            "hall_name":ticket.json()['hall_name'],
            "concert_id":ticket.json()['concert_id'],
            "concert_date":ticket.json()['concert_date']

        })

    return jsonify(
        {
            "code": 404,
            "message": "There are no concerts by that concert id."
        }
    ), 404


@app.route("/ticket/update/<string:concert_id>", methods=['PUT'])
def update_tickets(concert_id):
  
    ticket = Ticket.query.filter_by(concert_id=concert_id).first()
    
    data = request.get_json()
    print(data)
    print(ticket)
    if ticket:
        data = request.get_json()
        print(data)
        if data['chosen_cat1']:
            ticket.cat1_avail = ticket.cat1_avail-data['chosen_cat1']
        if data['chosen_cat2']:
            ticket.cat2_avail = ticket.cat2_avail-data['chosen_cat2']
        if data['chosen_cat3']:
            ticket.cat3_avail = ticket.cat3_avail-data['chosen_cat3']
        if data['chosen_cat4']:
            ticket.cat4_avail = ticket.cat4_avail-data['chosen_cat4']
        if data['chosen_cat5']:
            ticket.cat5_avail = ticket.cat5_avail-data['chosen_cat5']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": ticket.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Concert not found."
        }
    ), 404




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
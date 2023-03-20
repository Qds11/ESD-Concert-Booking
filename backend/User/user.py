from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)

# need to change DB uri accordingly
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/users'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'


    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    joined_date_time=db.Column(db.DateTime, nullable=False)
    birthdate=db.Column(db.DateTime,nullable=False)
    genre_preferred=db.Column(db.String(64),nullable=False)


    def __init__(self, user_id, username, email, contact, joined_date_time, birthdate, genre_preferred):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.contact = contact
        self.joined_date_time=joined_date_time
        self.birthdate=birthdate
        self.genre_preferred=genre_preferred


    def json(self):
        return {"user_id": self.user_id, "username": self.username, "email": self.email, "contact": self.contact, "joined_date_time":self.joined_date_time, "birthdate":self.birthdate, "genre_preferred":self.genre_preferred}


cors = CORS(app, resources={r'/*': {'origins': '*'}})

# hello world
@app.route('/', methods=['GET'])
def greetings():
    return ("Hello World")

# get all users
@app.route('/user', methods=['GET'])
def get_all():
    users = User.query.all()
    if len(users):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "users": [user.json() for user in users]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no users."
        }
    ), 404

# get username and userid with email
@app.route('/user/<string:email>', methods=['GET'])
def get_username_with_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user_id = user.user_id
        username = user.username
        return jsonify({
            "username": username,
            "userId": user_id
        })

    return jsonify(
        {
            "code": 404,
            "message": "There are no users with this email."
        }
    ), 404


#get specific user based on user_id
@app.route("/user/<string:user_id>")
def find_genre_by_user_id(user_id):
    print(user_id)
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify(
        {
            "code": 200,
            "message": user.json()['genre_preferred']
        }
    ), 200
    return jsonify(
        {
            "code": 404,
            "message": "Preferred Genre not found."
        }
    ), 404


# get birthday from user_id input
@app.route("/user/birthday/<string:user_id>")
def find_birthday_by_user_id(user_id):
    print(user_id)
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify(
        {
            "code": 200,
            "message": user.json()['birthdate']
        }
    ), 200
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404

# get phone number with user id
def get_phone_num(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify({
            "phone_num": user.json()['contact']
        }
    ), 200
    return jsonify({
        "code" : 404,
        "message": "User not found"
    }), 404
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
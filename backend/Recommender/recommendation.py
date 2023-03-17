from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/users'
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

@app.route("/user")
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
            "message": "There are no books."
        }
    ), 404



@app.route("/user/<string:user_id>")
def find_genre_by_user_id(user_id):
    print(user_id)
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        genre_preferred=user.json()['genre_preferred']
        return genre_preferred
    return jsonify(
        {
            "code": 404,
            "message": "Preferred Genre not found."
        }
    ), 404




if __name__ == '__main__':
    app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests
from invokes import invoke_http
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# for local db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/ticket_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)




@app.route("/user/<string:user_id>")
def find_genre_by_calling_user(user_id):
    results = invoke_http("http://localhost:5000/user/"+user_id, method='GET')
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











if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

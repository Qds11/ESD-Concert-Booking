from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests
from invokes import invoke_http
results = invoke_http("http://localhost:5000/user/1", method='GET')


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/ticket_db'
# # for local db
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/ticket_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

app = Flask(__name__)
CORS(app)

print( type(results) )
print()
print( results )








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

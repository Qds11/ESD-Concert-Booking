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





current_user_id='1'

# hello siyu i think this one is the duplicate code - ur secxiest friend clara

#api endpoint for concert ms to call, will call user ms and return the result from user to concert
@app.route("/user/<string:user_id>")
def find_genre_by_calling_user(user_id):
    results = invoke_http("http://127.0.0.1:5000/users/"+ user_id, method='GET')
    if results['code']==200:
        current_user_id=user_id
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

#find recommendation with concert id
@app.route("/recommendations/<string:concert_id>")
def find_recommendation(concert_id):
    results = invoke_http("http://127.0.0.1:5000/user/birthday/"+current_user_id, method='GET')
    birthdate=results['message']
    # convert to datetime object
    date_obj = datetime.strptime(birthdate, "%a, %d %b %Y %H:%M:%S %Z")

    # format the datetime object to desired format
    formatted_date = date_obj.strftime("%d/%m/%Y")

    # convert to datetime object
    date_obj = datetime.strptime(formatted_date, "%d/%m/%Y")

    # calculate age
    age = (date.today() - date_obj.date()).days // 365
    
    
    results = invoke_http("http://127.0.0.1:5004/avail/"+concert_id, method='GET')
    cat1=results['cat1_avail']
    cat2=results['cat2_avail']
    cat3=results['cat3_avail']
    cat4=results['cat4_avail']
    cat5=results['cat5_avail']
    
    hall_results = invoke_http("http://127.0.0.1:5004/hall/"+concert_id, method='GET')
    hall=hall_results['data']
    print(hall)

    # #here come the rules~~~
    recommendation_list=[]
    if cat2!=0 and cat2!=None and age>50:
        recommendation_list.append({'cat2':'Considering your comfort and concert experience, we recommend you this seating section nearest to the stage!'})
    elif cat1!=0 and cat1!=None and age<50:
        recommendation_list.append({'cat1':'We recommend this section as it is the nearest to the stage!'})
    elif cat2!=0 and cat2!=None and  hall!=3:
        recommendation_list.append({'cat2':'We recommend this section as it is the nearest non-standing seats for your comfort!'})
    elif cat2!=0 and cat2!=None and  hall==3:
        recommendation_list.append({'cat2':'We recommend this section as it is the nearest to stage!'})
    elif cat3!=0 and cat3!=None and  hall==3:
        recommendation_list.append({'cat2':'This is the last section left! Grab it Fast!'})
    elif cat3!=0 and cat3!=None:
        recommendation_list.append({'cat3':'We recommend this section which is the next nearest non-standing seats!'})
    elif cat4!=0 and cat4!=None:
        recommendation_list.append({'cat4':'We recommend this next best section as all the other sections are sold out.'})
    elif cat5!=0 and cat5!=None:
        recommendation_list.append({'cat3':'This is the last section left! Grab it Fast!'})
    else:
        recommendation_list.append('All Sold Out!')
        print(recommendation_list)
    if len(recommendation_list)!=0:
        return jsonify(
            {
                "code": 200,
                "recommendation": recommendation_list
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

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date
import requests
from invokes import invoke_http
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/halldata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)



#api endpoint for concert ms to call, will call user ms and return the result from user to concert
@app.route("/recommendations/user/<string:user_id>")
def find_genre_by_calling_user(user_id):
    results = invoke_http("http://localhost:8000/api/v1/user/genre/"+user_id +"?apikey=QRp2hItGLsgHXWD0CHVGBSHxJB6wEO7i", method='GET')
    print(results)
    if results['code']==200:
        global current_user_id
        current_user_id=user_id
        print(current_user_id)
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
@app.route("/recommendations/concert/<string:concert_id>")
def find_recommendation(concert_id):
    results = invoke_http("http://localhost:8000/api/v1/user/birthday/"+concert_id+"?apikey=QRp2hItGLsgHXWD0CHVGBSHxJB6wEO7i", method='GET')
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
    
  
    
    hall_results = invoke_http("http://127.0.0.1:5004/hall/"+concert_id, method='GET')

   
  

    # #here come the rules~~~
    if results['code']==200:
        recommendation_list=[]
        if results['cat2_avail']!=0 and results['cat2_avail']!=None and age>50:
            recommendation_list.append({'cat2':'Considering your comfort and concert experience, we recommend you this seating section nearest to the stage!'})
        elif results['cat1_avail']!=0 and results['cat1_avail']!=None and age<50:
            recommendation_list.append({'cat1':'We recommend this section as it is the nearest to the stage!'})
        elif results['cat2_avail']!=0 and results['cat2_avail']!=None and  hall_results['data']!=3:
            recommendation_list.append({'cat2':'We recommend this section as it is the nearest non-standing seats for your comfort!'})
        elif results['cat2_avail']!=0 and  results['cat2_avail']!=None and  hall_results['data']==3:
            recommendation_list.append({'cat2':'We recommend this section as it is the nearest to stage!'})
        elif results['cat3_avail']!=0 and results['cat3_avail']!=None and  hall_results['data']==3:
            recommendation_list.append({'cat2':'This is the last section left! Grab it Fast!'})
        elif  results['cat3_avail']!=None:
            if results['cat3_avail']!=0:
                recommendation_list.append({'cat3':'We recommend this section which is the next nearest non-standing seats!'})
        elif results['cat4_avail']!=None:
            if results['cat4_avail']!=0:
                recommendation_list.append({'cat4':'We recommend this next best section as all the other sections are sold out.'})
        elif results['cat5_avail']!=None:
            if results['cat5_avail']!=0:
                recommendation_list.append({'cat3':'This is the last section left! Grab it Fast!'})
        else:
            recommendation_list.append('All Sold Out!')
        return jsonify(
            {
                "code": 200,
                "recommendation": recommendation_list
            }
    ), 200
    
    return jsonify(
            {
                "code": 404,
                "message": "Recommendation not found."
            }
     ), 404

















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

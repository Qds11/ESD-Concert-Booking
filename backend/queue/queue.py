from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import requests
from invokes import invoke_http
import pika
import sys
from os import environ


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# for local db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/queue_database'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/queue_database'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


CORS(app)


class Queue(db.Model):
   queue_id = db.Column(db.Integer, nullable=False)
   user_id = db.Column(db.Integer, primary_key=True)
   status = db.Column(db.Enum('waiting', 'serving'), nullable=False)
   concert_id = db.Column(db.Integer, nullable=False, primary_key=True)
   expiration_time=db.Column(db.DateTime, nullable=True)



###### queue ui call this once to queue user regardless whether they actually need to queue####
@app.route('/queue', methods=['POST'])
def add_to_queue():
    try:
        # Check the number of rows with the status 'serving' (add seat selection page)
        serving_count = Queue.query.filter(
    Queue.status == 'serving',
    Queue.concert_id == request.json['concert_id'],
    Queue.expiration_time > datetime.now()
).count()
        #can only have 4 users at buying tix at once, if more than join queue
        # If more than 3 users at selection page then user to queue with 'waiting' status
        print(serving_count)
        if serving_count > 3:  #can change the limit in the future
            new_queue = Queue(status='waiting',
                              concert_id=request.json['concert_id'],
                              user_id=request.json['user_id'], expiration_time=None)
        else:  #else add user to queue with 'serving' status
            new_queue = Queue(status='serving',
                              concert_id=request.json['concert_id'],
                              user_id=request.json['user_id'], expiration_time=datetime.now() + timedelta(minutes=11))


        # Add new_queue to database
        db.session.add(new_queue)
        db.session.commit()
        return jsonify({'status': new_queue.status})
    except Exception as e:
        # return error status code and error message
        return jsonify({
            'status':
            'error',
            'message':
            "Error occurred when enqueueing user" + str(e)
        }), 400



##### queue iu freqeuently call this to updated queue position #####
@app.route('/waiting-queue/<int:user_id>/<int:concert_id>')
def waiting_queue(user_id, concert_id):
    try:
        user = Queue.query.filter_by(user_id=user_id,
                                     concert_id=concert_id).first()
        if user is None:
            return jsonify({
                'status': 'error',
                'message': 'User not found'
            }), 404


        if user.status == 'serving':
           user.expiration_time=datetime.now() + timedelta(minutes=11)
           db.session.commit()
           return jsonify({'queue_position': 0, 'status': 'serving'}), 200


        waiting_count = Queue.query.filter(
            Queue.status == 'waiting', Queue.concert_id == user.concert_id,
            Queue.queue_id < user.queue_id).count()

        if waiting_count == 3:
            print("waiting...")
            sendNotif(user_id)

        return jsonify({
            'queue_position': waiting_count + 1,
            'status': 'waiting'
        }), 200

    except Exception as e:
        return jsonify({
            'status':
            'error',
            'message':
            "Error occurred when getting user queue position: " + str(e)
        }), 500


###### seat selection UI call this if user exceed 10mins ######
#### payment call this once payment completed (btw, what happens if payment fails?)######
@app.route('/delete-from-queue/<int:user_id>/<int:concert_id>',
           methods=['DELETE'])
def delete_from_queue(user_id, concert_id):
    try:
        user = Queue.query.filter_by(user_id=user_id,
                                     concert_id=concert_id).first()
        queue_to_delete = Queue.query.filter_by(user_id=user_id,
                                                concert_id=concert_id).first()
        if not queue_to_delete:
            return jsonify({
                'message':
                'User with user_id ' + str(user_id) +
                ' queueing for concert_id ' + str(concert_id) +
                ' not found in queue',
                'status':
                'error'
            }), 404


        db.session.delete(queue_to_delete)
        db.session.commit()


        # if deleted user status is 'waiting' then just return message
        if user.status == 'waiting':
            return jsonify({
                'message':
                'User with user_id ' + str(user_id) + ' has been deleted'
            })

        # else update status of the person next in line to 'serving'
        serving_count = Queue.query.filter(Queue.status=='serving', Queue.concert_id==user.concert_id, Queue.expiration_time > datetime.now()).count()
        if serving_count < 4:
            earliest_waiting = Queue.query.filter_by(status='waiting', concert_id=user.concert_id).order_by(Queue.queue_id.asc()).first()
            if earliest_waiting:
                earliest_waiting.status = 'serving'
                earliest_waiting.expiration_time=datetime.now() + timedelta(minutes=11)
            db.session.commit()

        return jsonify({'status': 'success','message': 'User with user_id ' + str(user_id) + ' queueing for concert_id '+str(concert_id) +' has been deleted and queue status updated'})

    except Exception as e:
        # return error status code and error message
        return jsonify({'status': 'error', 'message': 'Error occurred when deleting from queue: ' + str(e)}), 500



def sendNotif(user_id):
    # 2. calls notification
    print('\n-----Invoking notification microservice-----')
    print(
        '\n\n-----Publishing the notif message with routing_key=queue.notif-----'
    )

    # notif_result = invoke_http('http://127.0.0.1:5100/sendQueueNotification/' + user_id, method='POST', json=user_id)

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='notif_topic', exchange_type='topic')

    routing_key = 'queue.notif'
    message = json.dumps(user_id)
    channel.basic_publish(exchange='notif_topic',
                        routing_key=routing_key,
                        body=message,
                        properties=pika.BasicProperties(delivery_mode=2)
                        )

    print(" [x] Sent %r:%r" % (routing_key, message))
    connection.close()

    print("\nRequest published to RabbitMQ Exchange.\n")


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5009, debug=True)

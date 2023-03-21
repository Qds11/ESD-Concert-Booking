from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://sql12606226:61vMwF9lhJ@sql12.freesqldatabase.com:3306/sql12606226'
# for local db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/queue_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('waiting', 'serving'), nullable=False)
    concert_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/queue', methods=['POST'])
def add_to_queue():
    # Check the number of rows with the status 'serving' (add seat selection page)
    serving_count = Queue.query.filter_by(status='serving',concert_id=request.json['concert_id']).count()
    #can only have 4 users at buying tix at once, if more than join queue
    # If more than 3 users at selection page then user to queue with 'waiting' status
    if serving_count > 3: #can change the limit in the future
        new_queue = Queue(status='waiting', concert_id=request.json['concert_id'])
    else: #else add user to queue with 'serving' status
        new_queue = Queue(status='serving', concert_id=request.json['concert_id'])

    # Add new_queue to database
    db.session.add(new_queue)
    db.session.commit()

    return jsonify({'id': new_queue.id,'status': new_queue.status})

#freqeuently call this to updated queue position
@app.route('/waiting-queue/<int:id>')
def waiting_queue(id):
    # Get the count of rows with the status 'waiting' who entered the queue earlier
    user = Queue.query.get(id)
    if(user.status=='serving'):
        return jsonify({'queue_position': 0})

    waiting_count = Queue.query.filter(Queue.status == 'waiting', Queue.concert_id==user.concert_id, Queue.created_at < user.created_at).count()
    return jsonify({'queue_position': waiting_count+1})

#delete user from queue table
@app.route('/delete-from-queue/<int:id>', methods=['DELETE'])
def delete_from_queue(id):
    user = Queue.query.get(id)
    queue_to_delete = Queue.query.get_or_404(id)
    db.session.delete(queue_to_delete)
    db.session.commit()
    # if deleted user status is 'waiting' then just return message
    if user.status=='waiting':
        return jsonify({'message': 'user with queue_id ' + str(id) + ' have been deleted'})

    #else update status of the person next in line to 'serving'
    serving_count = Queue.query.filter_by(status='serving',concert_id=user.concert_id).count()
    if serving_count < 4:
        earliest_waiting = Queue.query.filter_by(status='waiting',concert_id=user.concert_id).order_by(Queue.created_at.asc()).first()
        earliest_waiting.status = 'serving'
    db.session.commit()

    return jsonify({'message': 'user with queue_id ' + str(id) + ' have been deleted and queue status updated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
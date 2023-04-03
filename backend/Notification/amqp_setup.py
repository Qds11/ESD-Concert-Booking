import pika

hostname = "localhost" # default hostname
port = 5672 # default port
# connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port,
        heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
))

channel = connection.channel()

exchangename="order_topic"
exchangetype="topic"
channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

# Here can be a place to set up all queues needed by the microservices,
# - instead of setting up the queues using RabbitMQ UI.

############   Notification queue   #############

queue_name = 'Notification'
channel.queue_declare(queue=queue_name, durable=True) 
    # 'durable' makes the queue survive broker restarts

#bind Error queue
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.notif') 
    # bind the queue to the exchange via the key
    # any routing_key with two words and ending with '.notif' will be matched


"""
This function in this module sets up a connection and a channel to a local AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""
def check_setup():
    # The shared connection and channel created when the module is imported may be expired, 
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)


def is_connection_open(connection):

    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False

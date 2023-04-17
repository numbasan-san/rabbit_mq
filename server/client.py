
import pika, uuid

consumer_name = 'CLIENT'

def op_message_recive(ch, method, properties, body):
    print(f'{consumer_name}: recibibe {body}.')

conn_param = pika.ConnectionParameters('localhost')
con = pika.BlockingConnection(conn_param)
channel = con.channel()

reply_queue = channel.queue_declare(queue = 'letterbox', exclusive = True)
channel.basic_consume(queue = reply_queue.method.queue, auto_ack = True, on_message_callback = op_message_recive)
channel.queue_declare(queue = 'request-queue')

message = 'RIP AND TEAR UNTIL IT IS DONE!'
cor_id = str(uuid.uuid4())
print(f'Sending request to {cor_id}')
channel.basic_publish(
	exchange = '', 
	routing_key = 'request-queue', 
	properties = pika.BasicProperties(
		reply_to = reply_queue.method.queue,
		correlation_id = cor_id
	),
	body = message
)

print(f'sent message: {message}')

channel.start_consuming()

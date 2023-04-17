
import pika, time, random
from pika.exchange_type import *

exc_name = 'topic_exch'
que_name = ''

def op_message_recive(ch, method, properties, body):
    print(f'Order recibibe: {body}')
    ch.basic_publish(
        '', 
        routing_key = properties.reply_to,
        body = f'All right, {properties.correlation.id}'
    )

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange = exc_name, exchange_type = ExchangeType.topic)

queue = channel.queue_declare(queue=que_name, exclusive=True)

channel.queue_bind(exchange = exc_name, queue=queue.method.queue, routing_key = '#.payments')

channel.basic_consume(queue = queue.method.queue, auto_ack = True, on_message_callback = op_message_recive)

print('Start server.')
channel.start_consuming() 

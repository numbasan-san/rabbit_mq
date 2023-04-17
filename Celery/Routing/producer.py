
import pika
from pika.exchange_type import ExchangeType

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = 'This message needs to be routed'

channel.basic_publish(exchange='routing', routing_key='both', body=message)

print(f'sent message: {message}')

conn.close()

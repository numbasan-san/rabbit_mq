
import pika
from pika.exchange_type import ExchangeType

conn_param = pika.ConnectionParameters('localhost')
conn = pika.BlockingConnection(conn_param)
channel = conn.channel()

user_payments_message = 'A european user paid for something'

channel.basic_publish(exchange='topic', routing_key='user.europe.payments', body=user_payments_message)

print(f'sent message: {user_payments_message}')

business_order_message = 'A european business ordered goods'

channel.basic_publish(exchange='topic', routing_key='business.europe.order', body=business_order_message)

print(f'sent message: {business_order_message}')

conn.close()
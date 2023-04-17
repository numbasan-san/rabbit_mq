
import beat_conf

broker_url = 'amqp://localhost:5672'
result_backend = 'amqp://localhost:5672'
task_serializer = 'json'
result_serializer = 'json'
enable_utc = True
imports = (
    'tasks'
)

beat_shcedule = beat_conf


from celery import *
import celeryconfig

celery = Celery('celery_app')

celery.config_from_object('celeryconfig')

celery.conf.update(
    broker_url='amqp://localhost:5672',
    result_backend='amqp://localhost:5672',
    imports = (
        'tasks'
    )
)

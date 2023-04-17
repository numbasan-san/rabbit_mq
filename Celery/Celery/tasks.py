
import time, logging
from celery import *

app = Celery('tasks', broker='amqp://localhost:5672')
logger = logging.getLogger(__name__)

@app.task(queue = 'saludos')
def hello(name: str) -> str:
    time.sleep(0)
    logger.info(f"Hello {name}.")

@app.task
def suma(a: int, b: int):
    return (a + b)

@app.task
def veraz(a: bool):
    return f'Lo que dice es {a}'

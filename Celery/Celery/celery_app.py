
from celery import *
import celeryconfig

celery = Celery('ceelry_app')

celery.config_from_object('celery_app_with_beat.celeryconfig')

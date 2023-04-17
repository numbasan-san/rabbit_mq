
from celery.schedules import crontab

beat_conf = {
    "task_1": {
        "task": "celery_app_with_beat.scheduled_task_1",
        "schedule": crontab(minute = "*/1"),
    },
    "task_2": {
        "task": "celery_app_with_beat.scheduled_task_2",
        "schedule": crontab(minute = "*/1"),
    },
    "task_3": {
        "task": "celery_app_with_beat.scheduled_task_3",
        "schedule": crontab(minute = "*/1"),
        'options':{
            'queue': 'priority',
        }
    }
}

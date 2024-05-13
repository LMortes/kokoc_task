import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kokoc_task.settings')

app = Celery('kokoc_task')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': {
        'task': 'rates.tasks.get_values',
        'schedule': crontab(hour=7, minute=0),
        }
    }
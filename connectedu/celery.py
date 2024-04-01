from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectedu.settings')

app = Celery('connectedu')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# worker_cancel_long_running_tasks_on_connection_loss = True

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    return (f'Request: {self.request!r}')
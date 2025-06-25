import os

from celery import Celery

from library.tasks_scheduler import CELERY_BEAT_SCHEDULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_system.settings")

app = Celery("library_system")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

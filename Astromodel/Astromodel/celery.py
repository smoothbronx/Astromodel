from os import environ
from celery import Celery
from celery.schedules import crontab
from django.utils.timezone import datetime


environ.setdefault("DJANGO_SETTINGS_MODULE", (lambda value: value if value is not None else "Astromodel.settings.development")(environ.get("DJANGO_SETTINGS_MODULE")))

application = Celery("Astromodel")

application.config_from_object("django.conf:settings", namespace="CELERY")

application.autodiscover_tasks()

application.conf.beat_schedule = {
    "get-week-activity": {
        "task": "api.tasks.get_week_activity",
        "schedule": crontab(hour=23, minute=59, day_of_week='sun'),
        "args": datetime.today().isocalendar()
    }
}
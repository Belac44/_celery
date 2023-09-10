import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mock.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

from configurations import setup

setup()

app = Celery("mock")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


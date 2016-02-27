import os
from celery import Celery
from django.conf import settings


# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hiren.settings')
app = Celery('hiren')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


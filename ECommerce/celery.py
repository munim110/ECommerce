# django_email_marketing/celery.py
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerce.settings')

app = Celery('ECommerce')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
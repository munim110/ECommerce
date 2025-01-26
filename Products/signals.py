import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from datetime import datetime
from django.conf import settings

LOGS_DIR = os.path.join(settings.BASE_DIR, 'logs')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    try:
        action = 'created' if created else 'updated'
        log_path = os.path.join(LOGS_DIR, 'product_log.txt')
        with open(log_path, 'a') as f:
            f.write(f'{instance.name} was {action} at {datetime.now()}\n')
    except Exception as e:
        print(f"Signal error: {e}")

@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    try:
        log_path = os.path.join(LOGS_DIR, 'product_log.txt')
        with open(log_path, 'a') as f:
            f.write(f'{instance.name} was deleted at {datetime.now()}\n')
    except Exception as e:
        print(f"Signal error: {e}")
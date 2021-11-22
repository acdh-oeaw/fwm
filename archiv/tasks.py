import time
from celery import shared_task

from archiv.models import Geography


@shared_task
def count_geography(sleeping_seconds):
    time.sleep(sleeping_seconds)
    return Geography.objects.count()

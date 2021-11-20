from celery import shared_task

from archiv.models import Geography


@shared_task
def count_geography():
    return Geography.objects.count()

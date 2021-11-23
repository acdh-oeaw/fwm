import time
from celery import shared_task

from archiv.models import Geography
from appcreator.import_utils import run_import


@shared_task
def count_geography(sleeping_seconds):
    time.sleep(sleeping_seconds)
    return Geography.objects.count()


@shared_task
def ingest_data():
    file_class_map_dict = {
        'Sample': './archiv/data/Sample.csv'
    }
    run_import(
        'archiv',
        file_class_map_dict=file_class_map_dict,
        limit=1000,
    )
    return file_class_map_dict

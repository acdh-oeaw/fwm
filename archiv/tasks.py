import time
from django.apps import apps
from celery import shared_task

from archiv.models import Geography
from appcreator.import_utils import run_import


@shared_task
def count_geography(sleeping_seconds):
    time.sleep(sleeping_seconds)
    return Geography.objects.count()


@shared_task
def ingest_data(model_name):
    model = apps.get_model("archiv", model_name)
    file_class_map_dict = {model.__name__: model.get_source_table()}
    run_import(
        "archiv",
        file_class_map_dict=file_class_map_dict,
        limit=False,
    )
    return file_class_map_dict

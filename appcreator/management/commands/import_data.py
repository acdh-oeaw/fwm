from django.core.management.base import BaseCommand
from appcreator.import_utils import run_import

# imports for custom things


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        # file_class_map_dict = {
        #     'Sample': './archiv/data/Sample.csv'
        # }

        run_import(
            'archiv',
            file_class_map_dict=None,
            limit=10,
        )

import time

from django.core.management.base import BaseCommand

from archiv.models import Images


class Command(BaseCommand):
    help = "downlaods images"

    def handle(self, *args, **kwargs):
        pause = 5
        items = Images.objects.filter(image_stream=None)
        for idx, x in enumerate(items, start=1):
            x.pictures(verbose=True)
            if idx % 10 == 0:
                print(f"sleeping for {pause} seconds")
                time.sleep(pause)

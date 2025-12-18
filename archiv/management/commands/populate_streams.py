from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Images


class Command(BaseCommand):
    help = "removes binary stream data from Image"

    def handle(self, *args, **kwargs):
        items = Images.objects.all()
        for x in tqdm(items, total=items.count()):
            x.pictures()

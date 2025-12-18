import glob
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Images


class Command(BaseCommand):
    help = "removes binary stream data from Image"

    def handle(self, *args, **kwargs):
        image_dir = settings.IMAGES_DIR
        files = glob.glob(f"{image_dir}/*.webp")
        images = Images.objects.all()
        for x in tqdm(images, total=images.count()):
            x.image_stream = None
            x.save()
        for x in files:
            os.remove(x)

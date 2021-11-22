import pandas as pd
from tqdm import tqdm


from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point


from archiv.models import Geography


class Command(BaseCommand):
    help = "Import Coordinates"

    def handle(self, *args, **kwargs):
        source_file = Geography.get_source_table()
        df = pd.read_csv(source_file)
        df = df.drop(df[df.coordinates == 'x'].index)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            x, y = [float(x.strip()) for x in row['coordinates'].split('|')]
            geo = Geography.objects.get(name=row['name'])
            geo.coordinates = Point(y, x)
            geo.save()

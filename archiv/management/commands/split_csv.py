from django.core.management.base import BaseCommand

# imports for custom things
from tqdm import tqdm
import pandas as pd

SOURCE_FILE = './media/archiv/data/FWM_Daten.xlsx'
OUT_DIR = './archiv/data/'


class Command(BaseCommand):
    help = "Splits Execl with multiple sheets into CSV files"

    def handle(self, *args, **kwargs):
        excel = pd.ExcelFile(SOURCE_FILE)
        for x in tqdm(excel.sheet_names, total=len(excel.sheet_names)):
            df = pd.read_excel(SOURCE_FILE, sheet_name=x)
            df.to_csv(f'{OUT_DIR}/{x}.csv', index=False)

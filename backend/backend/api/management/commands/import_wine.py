import csv
from django.core.management.base import BaseCommand
from api.models import Wine

class Command(BaseCommand):
    help = 'Import wine data from CSV'

    def handle(self, *args, **kwargs):
        with open('C:\\Users\\Dave\\Desktop\\GatorBiome\\data\\wine.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            wines = []
            for row in reader:
                wine =  Wine(
            wine=int(row['Wine']),
            alcohol=float(row['Alcohol']),
            malate=float(row['Malic.acid']),
            ash=float(row['Ash']),
            acl=float(row['Acl']),
            mg=int(row['Mg']),
            phenols=float(row['Phenols']),
            flavanoids=float(row['Flavanoids']),
            nonflavanoids=float(row['Nonflavanoid.phenols']),
            proanth=float(row['Proanth']),
            color=float(row['Color.int']),
            hue=float(row['Hue']),
            OD=float(row['OD']),
            proline=int(row['Proline'])
        )
                wines.append(wine)
            Wine.objects.bulk_create(wines)
            self.stdout.write(self.style.SUCCESS('Successfully imported wine data'))

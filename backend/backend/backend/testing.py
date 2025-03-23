import pandas as pd
import csv
from ..api.models import Wine

with open ('C:\\Users\\Dave\\Desktop\\GatorBiome\\data\\wine.csv', r) as csvfile:
    reader = csv.DictReader(csvfile)
    print('ggg')
    for row in reader:
        Wine.objects.create(
            wine=int(row['wine']),
            alcohol=float(row['alcohol']),
            malate=float(row['malate']),
            ash=float(row['ash']),
            acl=float(row['acl']),
            mg=int(row['mg']),
            phenols=float(row['phenols']),
            flavanoids=float(row['flavanoids']),
            nonflavanoids=float(row['nonflavanoids']),
            proanth=float(row['proanth']),
            color=float(row['color']),
            hue=float(row['hue']),
            OD=float(row['OD']),
            proline=int(row['proline'])
        )

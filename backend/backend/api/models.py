from django.db import models


# Create your models here.
class Wine(models.Model):
    wine = models.IntegerField()
    alcohol = models.FloatField()
    malate = models.FloatField()
    ash = models.FloatField()
    acl = models.FloatField()
    mg = models.IntegerField()
    phenols = models.FloatField()
    flavanoids = models.FloatField()
    nonflavanoids = models.FloatField()
    proanth = models.FloatField()
    color = models.FloatField()
    hue =models.FloatField()
    OD = models.FloatField()
    proline = models.IntegerField()

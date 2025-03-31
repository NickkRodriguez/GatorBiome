from django.db import models


class MLModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Dataset(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ModelMetrics(models.Model):
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name='metrics')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='model_metrics')

    auc = models.FloatField()
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    f1 = models.FloatField()

    class Meta:
        unique_together = ('model', 'dataset')
        verbose_name_plural = 'Model Metrics'

    def __str__(self):
        return f"{self.model} on {self.dataset}"

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

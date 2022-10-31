from django.db import models

# Create your models here.
class Car(models.Model):
    BrandName = models.CharField(max_length=100)
    ModelName = models.CharField(max_length=100)
    FuelType = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.BrandName

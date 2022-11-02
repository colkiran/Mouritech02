from django.db import models

# Create your models here.
class Product(models.Model):
    Prodid = models.CharField(max_length=7, unique=True)
    Prodname = models.CharField(max_length=50)
    Category = models.CharField(max_length=25)
    Prodtype = models.CharField(max_length=25)
    Price = models.FloatField()
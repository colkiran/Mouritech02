from django.db import models


class Category(models.Model):
    Categoryid = models.CharField(max_length=10)
    Categoryname = models.CharField(max_length=50)

# Create your models here.
class Product(models.Model):
    prodid = models.CharField(max_length=7, unique=True)
    Prodname = models.CharField(max_length=50)
    Categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    Prodtype = models.CharField(max_length=30)
    Price = models.FloatField()



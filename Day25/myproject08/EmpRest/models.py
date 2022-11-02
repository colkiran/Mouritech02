from django.db import models

# Create your models here.
class Employee(models.Model):
    Empname = models.CharField(max_length=50)
    Deptname = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Age = models.IntegerField()
    Salary = models.FloatField()

    def __str__(self):
        return self.Empname
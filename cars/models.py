from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=225)
    model = models.CharField(max_length=225)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
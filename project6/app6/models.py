from django.db import models
from datetime import datetime

class Product(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    mfr_date = models.DateField()
    exp_date = models.DateField()
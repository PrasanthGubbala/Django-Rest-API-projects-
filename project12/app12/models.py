from django.db import models

class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()
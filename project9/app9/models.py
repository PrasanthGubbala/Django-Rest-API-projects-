from django.db import models

class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()

class EmployeeModel(models.Model):
    e_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,max_length=30)
    designation = models.CharField(max_length=30)
    exp = models.IntegerField()
    salary = models.IntegerField()
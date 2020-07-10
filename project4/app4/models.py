from django.db import models

class Employee(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    salary = models.FloatField()
    date_of_join = models.DateField()
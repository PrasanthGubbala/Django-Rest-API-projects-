from django.db import models

class Course(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    fee = models.IntegerField()

class Common(models.Model):
    indo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    subject = models.CharField(max_length=30)
    class Meta:
        abstract = True

class Faculty(Common):
    subject = models.ManyToManyField(Course)
    salary = models.IntegerField()
class Student(Common):
    subject = models.ManyToManyField(Course)
    fee = models.IntegerField()
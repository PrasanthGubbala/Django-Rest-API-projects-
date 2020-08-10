from django.db import models

class ProviderDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    contact = models.IntegerField(unique=True)
    address = models.TextField()
    email = models.EmailField(unique=True,primary_key=True)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='provider_photo')



from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

admin.site.register(Product)

admin.site.unregister(User)
admin.site.unregister(Group)

from rest_framework import serializers
from .models import ProductModel
import re

class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1000.00)
    def validate_data(self, name):
        result = re.findall(r"^[A-Z a-z,0-9]*$",name)
        if result:
            return result
        else:
            raise serializers.ValidationError('Invalid Name')
    class Meta:
        model = ProductModel
        fields = '__all__'

from rest_framework import serializers
from app12.models import ProductModel
import re

class ProductSerializer(serializers.ModelSerializer):
    def validate_name(self,name):
        result = re.findall(r'^[A-Z a-z,0-9]*$',name)
        if result:
            return result[0]
        else:
            raise serializers.ValidationError('Product Name Shoud Contain Only Alphabets If Require Digits Also')
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1000.00)
    class Meta:
        model = ProductModel
        fields = '__all__'
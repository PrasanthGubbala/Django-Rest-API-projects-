import re

from rest_framework import serializers

from app11.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1000.00)
    def validate_name(self,name):
        result = re.findall(r'^[A-Z a-z,0-9]*$',name)
        if result:
            return result[0]
        else:
            raise serializers.ValidationError('Invalid Entered Name')
    class Meta:
        model = ProductModel
        fields = '__all__'
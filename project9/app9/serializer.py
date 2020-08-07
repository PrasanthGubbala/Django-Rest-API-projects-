from django.db.utils import IntegrityError
from  rest_framework import serializers
from app9.models import ProductModel,EmployeeModel
import re

#custom validations
def validate_name(name):
    result = re.findall(r"^[A-Z a-z]*$",name)
    if result:
        return result[0]
    else:
        raise serializers.ValidationError('Invalid Input- it must contain only alphabets either capital or small')

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[validate_name])
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1000.00)

    def create(self, validated_data):
        try:
            return ProductModel.objects.create(**validated_data)
        except:
            raise serializers.ValidationError('Invalid Input')


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30,validators=[validate_name])
    designation = serializers.CharField(max_length=30,validators=[validate_name])
    exp = serializers.IntegerField(min_value=1,max_value=20)
    salary = serializers.IntegerField(min_value=100000.00,max_value=1200000.00)

    def create(self, validated_data):
        try:
            return ProductModel.objects.create(**validated_data)
        except:
            raise serializers.ValidationError('Invalid Input')

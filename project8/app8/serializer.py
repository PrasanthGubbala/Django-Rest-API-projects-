from rest_framework import serializers
from app8.models import ProductModel

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=1000.00)

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

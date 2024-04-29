from rest_framework import serializers
from .models import *



class ProductSRL(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSRL(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class GetSRL(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all___'


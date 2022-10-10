from rest_framework import serializers
from .models import *
from rest_framework.response import Response

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
         model = Product
         fields = '__all__'
         
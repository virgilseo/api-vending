from django.shortcuts import render
from . models import *
from .serializers import*
from rest_framework import generics

# Create your views here.

class ProductListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    

class ProductDetailView(generics.RetrieveAPIView,
                        generics.DestroyAPIView,
                        generics.UpdateAPIView):
      
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
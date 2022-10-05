from django.shortcuts import render
from . models import *
from .serializers import*
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ProductListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class ProductDetailView(generics.RetrieveAPIView,
                        generics.DestroyAPIView,
                        generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

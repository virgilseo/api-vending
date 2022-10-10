from django.shortcuts import render
from . models import *
from .serializers import*
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import UserProfile
import json

# Create your views here.


class ProductListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        response = {}
        status = 0
        instance = self.get_object()
        if instance.sellerId == self.request.user.id: 
            self.perform_destroy(instance)
            response['message'] = 'Product was deleted from your account' 
            status = 200
        else:
            response['message'] = 'Not your product' 
            status = 401
        return Response(response, status=status)
    
    def patch(self, request, *args, **kwargs):
        response = {}
        status = 0
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.sellerId == self.request.user.id:
            return self.partial_update(request, *args, **kwargs)
        else:
            response['message'] = 'Not your product' 
            status = 401
            return Response(response, status=status)


class ProductBuyView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        response = {}
        profile = UserProfile.objects.get(user=request.user)
        productId = request.data['productId']

        if profile.role == 'buyer':
            product = Product.objects.get(id=productId)
            availableBalance = profile.deposit
            # check for sufficient ballance and product availability
            if product.amountAvailable == 0:
                response['message'] = 'Not enough products left'

            elif profile.deposit >= product.cost:
                profile.deposit = 0
                profile.save()

                product.amountAvailable = product.amountAvailable - 1
                product.save()

                response['product'] = {
                    'name':  product.productName,
                    'cost': product.cost,
                    'available': product.amountAvailable
                }
                response['change'] = availableBalance - product.cost
                response['spent'] = product.cost
            elif profile.deposit < product.cost:
                response['message'] = 'Please deposit more coins'

        else:
            response['message'] = 'Only users with buyer role can make a purchase'

        return Response(response)

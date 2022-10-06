from django.shortcuts import render
from . models import *
from .serializers import*
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import UserProfile

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


class ProductBuyView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        response = {}
        profile = UserProfile.objects.get(user=request.user)
        productId = request.data['productId']
        productAmount = request.data['productAmount']

        if profile.role == 'buyer':
            product = Product.objects.get(id=productId)
            availableBalance = profile.deposit
            # check for sufficient ballance and product availability
            if profile.deposit >= (productAmount * product.cost) and productAmount <= product.amountAvailable:
                profile.deposit = 0
                profile.save()

                product.amountAvailable = product.amountAvailable - productAmount
                product.save()

                response['product'] = {
                    'name':  product.productName,
                    'cost': product.cost,
                    'available': product.amountAvailable
                }
                response['amount'] = productAmount
                response['change'] = availableBalance - \
                    (product.cost * productAmount)
                response['spent'] = product.cost * productAmount
            elif productAmount >= product.amountAvailable:
                response['message'] = 'Not enough products left'
            else:
                response['message'] = 'Please deposit more coins'

        else:
            response['message'] = 'Only users with buyer role can make a purchase'

        return Response(response)

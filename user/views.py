from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

class UserView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

## Customize jwt claim - add user details and profile
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add extra responses here
        data['username'] = self.user.username
        
        profile = UserProfile.objects.filter(user=self.user)[0]
        
        data['role'] = profile.role
        data['deposit'] = profile.deposit
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
class UserDepositView(APIView):
    permission_classes = (IsAuthenticated,)    
            
    def post(self, request, format=None):
        response ={}
        profile = UserProfile.objects.filter(user=request.user)[0]
        ## check for appropriate coins
        deposits = [5, 10, 20, 50, 100]
        properDeposit = True
        if request.data['deposit'] not in deposits:
            properDeposit = False
        
        if profile.role == 'buyer':
            if properDeposit == True:
                profile.deposit = request.data['deposit'] + profile.deposit
                profile.save()
                
                response['balance'] = profile.deposit
            else:
                response['message'] = 'Only 5, 10, 20, 50 or 100 coins are acceptable'
            
        else:
            
            response['message'] = 'Only buyers can deposit coins'
            response['status'] = 400
        
        return Response(response)
    
class DepositResetView(APIView):
    permission_classes = (IsAuthenticated,)  
    
    def post(self, request, format=None):
        response ={}
        profile = UserProfile.objects.filter(user=request.user)[0]
        
        if profile.role == 'buyer':
            profile.deposit = 0
            profile.save()
            
            response['message'] = 'Success'
            response['balance'] = profile.deposit
            
        else:
            request.status_code = 400
            response['message'] = 'Only buyers can reset their deposit'
        
        return Response(response)
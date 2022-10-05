from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your views here.

class UserView(generics.CreateAPIView):
   queryset = UserProfile.objects.all()
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
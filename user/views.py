from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *

# Create your views here.

class UserView(generics.CreateAPIView):
   queryset = UserProfile.objects.all()
   serializer_class = UserSerializer

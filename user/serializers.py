from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']))
        
        UserProfile.objects.create(user=user)
        UserProfile.objects.filter(user=user).update(
            role = validated_data['profile']['role']
        )

        return user

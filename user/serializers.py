from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


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
        response = {}
        profile = validated_data.pop('profile')

        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']))

        UserProfile.objects.create(
            user=user,
            role=profile['role']
        )

        return user

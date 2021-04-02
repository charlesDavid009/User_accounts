from rest_framework import serializers
from .models import User



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required= True)
    password2 = serializers.CharField(label = "confirm password", required= True)
    class Meta:
        models = User
        fields = ['username', 'email', 'password', 'password2', 'telephone', 'role',]
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}
                        }

    def validate(self, attrs):
        """
        VALIDATING NEW USER Password
        """
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                {"Details": "Those passwords doesn't match"})
        return password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

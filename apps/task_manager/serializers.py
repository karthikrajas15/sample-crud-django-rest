# Django LIB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# rest framework LIB
from rest_framework import serializers

# Local DIR LIB
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8,style={'input_type': 'password'}, label="Password")
    confirm_password = serializers.CharField(style={'input_type': 'password'}, label="Confirm Password")

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    def validate(self, data):
        if data.get('email'):
            data['username'] = data.get('email')
            user = User.objects.filter(email=data.get('email'))
            if user:
                raise serializers.ValidationError({'email': ["Email Already exists.Please give different email."]})
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password and Confirm password not match.")
        data.pop('confirm_password')
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, style={'input_type': 'password'}, label="Password")

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        if data.get('email'):
            user = User.objects.filter(email=data['email'])
            if user:
                auth_user = authenticate(username=user.first().username, password=data['password'])
                if auth_user:
                    raise serializers.ValidationError("Incorrect Email or Password")
            else:
                raise serializers.ValidationError("Incorrect Email or Password")
        return data

class TaskListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = "__all__"

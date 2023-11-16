from rest_framework import serializers
from .models import CustomUser
# from CustomUserPermissions.serializers import PermissionSerializer
from django.contrib.auth.hashers import make_password, check_password


class LoginSignupCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name',]

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'profile_image', 'wallet']

class UpdateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'profile_image']
        
class UpdateCustomUserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'wallet']

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User
from rest_framework.validators import UniqueValidator

class LoginSerializer(serializers.Serializer):
    """User login serializer"""
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """Check credentials."""
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('invalid_credentials')
        
        return data

class SingUpSerializer(serializers.Serializer):
    """User sing up serializer"""
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    mobile_number = serializers.CharField(min_length=8, max_length=14)
    password = serializers.CharField(min_length=8, max_length=20)

    def create(self, data):
        """Handle user creation"""
        user = User.objects.create(**data)
        user.set_password(data['password'])
        user.is_staff = True
        user.save()

        return user   
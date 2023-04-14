#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """     
    Serializer of model User
    params: class of serializer model
    """
    class Meta:
        model = User 
        fields = (
            'email', 
            'mobile_number',
            'password'
        )

    def create(self, data):
        """
        Create User
        params: self and data received
        """
        user = User(
            email = data['email'].lower(),
            password = data['password'],
        )
        user.set_password(data['password'])
        user.save()
        
        return user     

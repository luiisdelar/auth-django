from .models import User
from rest_framework import generics
from users.serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    """
    Class for list users
    params: predefined class 
    """
    serializer_class = UserSerializer
    permission_classes = ''
    
    def get_queryset(self):
        """
        Queryset of list users
        """
        return User.objects.all()
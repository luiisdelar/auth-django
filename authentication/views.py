from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer, SingUpSerializer
from rest_framework.response import Response
from rest_framework import status

class Login(APIView):
    """User login API view"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception = True):
            return Response(status = status.HTTP_200_OK)

class SingUp(APIView):
    """SignUp view"""
    serializer_class = SingUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'message': 'user_successfully_created'}, status = status.HTTP_201_CREATED)
        else:
            return Response({ 'message': 'failed_to_create_user'}, status = status.HTTP_422_UNPROCESSABLE_ENTITY)

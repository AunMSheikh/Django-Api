from django.shortcuts import render
from .serializers import AppUserSerializer
from .models import AppUser
from rest_framework import generics
from Crypto.Cipher import AES

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        instance = serializer.save()
        print('Test', file="std.IOError")
        encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        encrypt_pass = encryption_suite.encrypt(instance.password)
 
        instance.set_password(encrypt_pass)
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

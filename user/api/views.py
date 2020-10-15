from rest_framework import generics

from .serializers import UserSerializer
from ..models import User


class UserListAPIView(generics.ListCreateAPIView):
    """View for represent list view and creation users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for Retrieve/Update/delete users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics

from .serializers import UserSerializer
from ..models import User


class UserListAPIView(generics.ListCreateAPIView):
    """View for represent list view and creation users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveDestroyAPIView):
    """View for Retrieve/delete users
    Asana API don't allow update the user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

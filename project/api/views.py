from rest_framework import generics

from .serializers import ProjectSerializer
from ..models import Project

from servises.asana_connect import client_connect

asana_client = client_connect()


class ProjectListAPIView(generics.ListCreateAPIView):
    """View for represent list view and creation"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for Retrieve/Update/delete projects"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

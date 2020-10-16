from rest_framework import generics

from .serializers import TaskSerializer
from ..models import Task


class TaskListAPIView(generics.ListCreateAPIView):
    """View for represent list view and creation tasks"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for Retrieve/Update/delete tasks"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from rest_framework import serializers

from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Model to represent Asana Task"""

    class Meta:
        model = Task
        fields = ('id', 'description', 'assignee', 'projects',)

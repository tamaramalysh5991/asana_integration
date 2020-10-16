from rest_framework import serializers

from servises.asana_connect import client_connect
from ..models import Task

asana_client = client_connect()


class TaskSerializer(serializers.ModelSerializer):
    """Model to represent Asana Task"""

    class Meta:
        model = Task
        fields = ('description', 'assignee', 'projects')

    def save(self, **kwargs):
        instance = super().save()
        task = asana_client.tasks.create(
            {
                'name': instance.description,
                'assignee': instance .assignee.gid,
                'projects': [project.gid for project in instance.projects.all()]
            }
        )
        instance .gid = task['gid']
        instance .save()

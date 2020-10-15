from django.db import transaction
from rest_framework import serializers
from ..models import Project

from servises.asana_connect import client_connect

asana_client = client_connect()


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Asana project"""

    class Meta:
        fields = ('id', 'name', 'workspace')
        model = Project

    def save(self, **kwargs):
        with transaction.atomic():
            asana_client.projects.create(
                {'name': self.validated_data['name'],
                 'workspace': self.validated_data['workspace']})
            super().save(**kwargs)

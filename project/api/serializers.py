from rest_framework import serializers
from ..models import Project
from servises.asana_connect import client_connect, get_workspace

asana_client = client_connect()


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Asana project"""

    workspace = serializers.CharField(allow_blank=True)

    class Meta:
        fields = ('id', 'name', 'workspace',)
        model = Project


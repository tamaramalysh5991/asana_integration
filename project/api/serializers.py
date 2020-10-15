from rest_framework import serializers
from ..models import Project
from django.conf import settings
from servises.asana_connect import client_connect

asana_client = client_connect()


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Asana project"""

    workspace = serializers.CharField(allow_blank=True)

    class Meta:
        fields = ('id', 'name', 'workspace')
        model = Project

    def validate_workspace(self, value):
        workspace = value or getattr(settings, 'ASANA_WORKSPACE', None)
        if not workspace:
            raise serializers.ValidationError("Asana workspace is required")
        return workspace

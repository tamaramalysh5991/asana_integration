from rest_framework import serializers
from ..models import Project
from django.conf import settings
from servises.asana_connect import client_connect

asana_client = client_connect()


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Asana project"""

    workspace = serializers.CharField(allow_blank=True)
    gid = serializers.CharField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'workspace', 'gid')
        model = Project

    def validate_workspace(self, value):
        """Try to get workspace from request data or settings
        Every project is required to be created in a specific workspace or
        organization, and this cannot be changed once set.
        https://developers.asana.com/docs/create-a-project
        """
        workspace = value or getattr(settings, 'ASANA_WORKSPACE', None)
        if not workspace:
            raise serializers.ValidationError("Asana workspace is required")
        return workspace

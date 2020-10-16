from rest_framework import serializers
from ..models import User

from servises.asana_connect import client_connect

asana_client = client_connect()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Asana User"""
    gid = serializers.CharField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'gid')
        model = User

from django.db import models

from core.models import AsanaModel
from servises.asana_connect import client_connect

asana_client = client_connect()


class Project(AsanaModel):
    """Model to represent Asana Project"""
    name = models.CharField(verbose_name='Project Name', max_length=1024)
    workspace = models.CharField(
        max_length=24, blank=True,
    )

    def __str__(self):
        return f'Project {self.name}'

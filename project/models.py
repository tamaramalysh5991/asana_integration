from django.db import models

from servises.asana_connect import client_connect

asana_client = client_connect()


class Project(models.Model):
    """Model to represent Asana Project"""
    name = models.CharField(verbose_name='Project Name', max_length=1024)
    workspace = models.CharField(
        max_length=24, blank=True,
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        asana_client.projects.create(
            {
                'name': self.name,
                'workspace': self.workspace
            }
        )
        super().save(force_insert, force_update, using, update_fields)

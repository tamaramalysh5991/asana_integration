import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from servises.asana_connect import client_connect
from .models import Project

asana_client = client_connect()
logger = logging.getLogger('django')


@receiver(post_save, sender=Project)
def create_asana_project(sender, instance, created, **kwargs):
    """Create or update a asana  project instance"""
    if created:
        project = asana_client.projects.create(
            {
                'name': instance.name,
                'workspace': instance.workspace
            }
        )
        instance.gid = project['gid']
        logger.info(f'Asana project was created {project}')
        return

    project = asana_client.projects.update_project(
        instance.gid, {'name': instance.name},
    )
    logger.info(f'Asana project was updated {project}')

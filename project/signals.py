import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from servises.asana_connect import client_connect, get_workspace
from .models import Project

asana_client = client_connect()
logger = logging.getLogger('django')


@receiver(post_save, sender=Project)
def create_asana_project(sender, instance, created, **kwargs):
    """Create or update a asana  project instance"""
    if created:
        workspace = instance.workspace or get_workspace(client=asana_client)
        # TODO: need better solution if workspace was not provided
        if not workspace:
            logger.error('Workspace was not provided')
            return
        project = asana_client.projects.create(
            {
                'name': instance.name,
                'workspace': workspace
            }
        )
        Project.objects.filter(
            id=instance.id).update(gid=project['gid'], workspace=workspace)
        logger.info(f'Asana project was created {project}')
    else:
        project = asana_client.projects.update_project(
            instance.gid, {'name': instance.name},
        )
        logger.info(f'Asana project was updated {project}')

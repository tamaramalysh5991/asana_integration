import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from servises.asana_connect import client_connect, get_workspace
from .models import User

asana_client = client_connect()
logger = logging.getLogger('django')


@receiver(post_save, sender=User)
def create_asana_profile(sender, instance, created, **kwargs):
    """Create a asana user instance"""
    if created:
        workspace = instance. workspace or get_workspace(client=asana_client)
        # TODO: need better solution if workspace was not provided
        if not workspace:
            logger.error('Workspace was not provided')
            return
        user = asana_client.workspaces.add_user_for_workspace(
            workspace, {'user': instance.name, }
        )
        User.objects.filter(id=instance.id).update(
            gid=user['gid'], workspace=workspace)
        logger.info(f'Asana user was created {user}')

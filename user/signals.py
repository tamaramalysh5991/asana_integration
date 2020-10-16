from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from servises.asana_connect import client_connect
from .models import User

asana_client = client_connect()


@receiver(post_save, sender=User)
def create_asana_profile(sender, instance, created, **kwargs):
    """Create a asana user instance"""
    if created:
        user = asana_client.workspaces.add_user_for_workspace(
            settings.ASANA_WORKSPACE, {'user': instance.name, }
        )
        instance.gid = user['gid']

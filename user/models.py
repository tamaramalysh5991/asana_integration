from django.contrib.auth import get_user_model
from django.db import models

from servises.asana_connect import client_connect
from django.conf import settings

DjangoUser = get_user_model()

asana_client = client_connect()


class User(models.Model):
    """Custom user model to represent Asana User.
    Note this is not related to a django User (although you can establish a
    relationship yourself).
    """
    name = models.CharField('name', max_length=1024)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        asana_client.workspaces.add_user_for_workspace(
            settings.ASANA_WORKSPACE, {'user': self.name, }
        )
        super().save(force_insert, force_update, using, update_fields)

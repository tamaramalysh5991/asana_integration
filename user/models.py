from django.contrib.auth import get_user_model
from django.db import models

from core.models import AsanaModel
from servises.asana_connect import client_connect

DjangoUser = get_user_model()

asana_client = client_connect()


class User(AsanaModel):
    """Custom user model to represent Asana User.
    Note this is not related to a django User (although you can establish a
    relationship yourself).
    """
    name = models.CharField('name', max_length=1024)

from django.contrib.auth import get_user_model
from django.db import models

DjangoUser = get_user_model()


class User(models.Model):
    """Custom user model to represent Asana User.
    Note this is not related to a django User (although you can establish a
    relationship yourself).
    """
    name = models.CharField('name', max_length=1024)


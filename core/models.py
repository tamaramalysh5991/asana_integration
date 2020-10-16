from django.db import models

class AsanaModel(models.Model):
    """An abstract base class for Asana models."""
    gid = models.CharField(
        max_length=31,
        db_index=True,
        null=True,
        help_text='The gid of this object in Asana.'
    )

    class Meta:
        abstract = True

from django.db import models


class Project(models.Model):
    """Model to represent Asana Project"""
    name = models.CharField(verbose_name='Project Name')

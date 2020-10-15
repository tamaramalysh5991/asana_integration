from django.db import models
from user.models import User
from project.models import Project


class Task(models.Model):
    """Model to represent Asana Task

    Attributes:
        projects: in Asana the task can be related to many porjects
        description: task text
        assignee: user who assigned to this task
    """
    projects = models.ManyToManyField(
        Project,
        related_name='tasks'
    )
    description = models.TextField(verbose_name='Task description')
    assignee = models.ForeignKey(
        User, verbose_name='Assignee',
        related_name='assigned_tasks',
        null=True,
        on_delete=models.SET_NULL
    )

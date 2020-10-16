import logging

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from project.models import Project
from servises.asana_connect import client_connect
from .models import Task

asana_client = client_connect()
logger = logging.getLogger('django')


def remove_projects_from_task(task: Task, project_ids: set):
    """Remove projects from task in Asana"""
    projects = Project.objects.filter(id__in=project_ids)
    if not projects:
        return
    for project in projects.all():
        result = asana_client.tasks.remove_project_for_task(
            task.gid, {
                'project': project.gid
            },
        )
        logger.info(f'Project {project.gid} removed from task {result}')


def add_new_projects(task: Task):
    """Add the new added project to Asana task"""
    for project in task.projects.all():
        asana_client.tasks.add_project_for_task(
            task.gid, {
                'project': project.gid
            },
        )


def create_asana_task(task: Task):
    """Create the task in Asana after db creation"""
    asana_task = asana_client.tasks.create(
        {
            'name': task.description,
            'assignee': task.assignee.gid,
            'projects': [
                project.gid for project in task.projects.all()
            ]
        }
    )
    Task.objects.filter(id=task.id).update(gid=asana_task['gid'])
    logger.info(f'Asana task was created {task}')
    return


@receiver(m2m_changed, sender=Task.projects.through)
def change_asana_task_project(sender, **kwargs):
    """Update a asana task instance projects
    In asana the task can have one or more projects
    So, need to delete and update it directly
    """
    instance = kwargs.pop('instance', None)
    pk_set = kwargs.pop('pk_set', None)
    action = kwargs.pop('action', None)

    if not instance.gid and action == 'post_add':
        create_asana_task(instance)
    if instance.gid and action == 'post_add':
        add_new_projects(task=instance)
    if action == 'post_remove':
        remove_projects_from_task(task=instance, project_ids=pk_set)


@receiver(post_save, sender=Task)
def update_asana_task(sender, instance, created, **kwargs):
    """Update a asana  task instance"""
    if created:
        return

    task = asana_client.tasks.update_task(
        instance.gid, {
            'name': instance.description,
            'assignee': instance.assignee.gid,
        },
    )
    logger.info(f'Asana task was updated {task}')

from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task'

    def ready(self):
        """Load signals on app ready"""
        from . import signals # noqa

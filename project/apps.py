from django.apps import AppConfig


class ProjectConfig(AppConfig):
    name = 'project'

    def ready(self):
        """Load signals on app ready"""
        from . import signals # noqa
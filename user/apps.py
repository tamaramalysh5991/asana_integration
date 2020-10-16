from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        """Load signals on app ready"""
        from . import signals # noqa

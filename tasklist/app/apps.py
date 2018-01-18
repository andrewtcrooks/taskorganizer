"""apps.py ."""
from django.apps import AppConfig


app_name = 'tasklist.app'


class UserConfig(AppConfig):
    """UserConfig app."""

    name = 'user'
    verbose_name = "User"


class TaskConfig(AppConfig):
    """TaskConfig app."""

    name = 'task'
    verbose_name = "Task"

from django.apps import AppConfig


app_name = 'tasklist.app'

class UserConfig(AppConfig):
    name = 'user'
    verbose_name = "User"

class TaskConfig(AppConfig):
    name = 'task'
    verbose_name = "Task"
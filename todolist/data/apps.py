from django.apps import AppConfig


app_name = 'todolist.data'

class UserConfig(AppConfig):
    name = 'user'
    verbose_name = "User"

class TodoConfig(AppConfig):
    name = 'todo'
    verbose_name = "Todo"
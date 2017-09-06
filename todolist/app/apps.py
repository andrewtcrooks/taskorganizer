from django.apps import AppConfig


app_name = 'todolist.app'

class ListConfig(AppConfig):
    name = 'list'
    verbose_name = "List"

class ItemConfig(AppConfig):
    name = 'item'
    verbose_name = "Item"
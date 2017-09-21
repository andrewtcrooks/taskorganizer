from django.db import models
from django.utils import timezone

app_name = 'todolist.data'


#class TodoManager(models.Manager):
#    """There should be a doc string here."""#

#    def get_queryset(self):
#        return super(TodoManager, self).get_queryset().filter(complete=False)




class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    password = models.CharField(max_length=200)
    join_date = models.DateTimeField(editable=False,default=timezone.now)
    #profile_pic = models.ImageField(upload_to = 'users/', blank=True, default='default.png')

class Todo(models.Model):
    todo_job = models.TextField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey('User')
    #incomplete_tasks = TaskManager()
    #objects = models.Manager()

    #def __repr__(self):
    #    output = "<job: {} complete: {}>"
    #    return output.format(self.todo_job, self.complete)

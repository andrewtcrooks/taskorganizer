"""models.py ."""
from django.db import models
from django.utils import timezone


app_name = 'tasklist.app'


class User(models.Model):
    """User model."""

    first_Name = models.CharField(max_length=255)
    last_Name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=200)
    join_date = models.DateTimeField(editable=False, default=timezone.now)
    # profile_pic = models.ImageField(upload_to = 'users/', blank=True,
    # default='default.png')


class Task(models.Model):
    """Task model."""

    task_job = models.TextField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE,)

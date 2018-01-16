"""Test models."""

from django.test import TestCase
from django.models import (CharField, EmailField, DateTimeField,
                           TextField, BooleanField, ForeignKey)
from tasklist.app.models import User, Task


class UserTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Set up."""
        User.objects.create(first_Name="Bob",
                            last_Name="Smith",
                            email="bob.smith@test.com",
                            password="passwrd",
                            join_date=""
                            )

    def test_model_fields(self):
        """Test."""
        user_objects = User.objects.get(first_Name="Bob")
        self.assertIsInstance(user_objects.first_Name, CharField, msg=None)
        self.assertIsInstance(user_objects.last_Name, CharField, msg=None)
        self.assertIsInstance(user_objects.email, EmailField, msg=None)
        self.assertIsInstance(user_objects.password, CharField, msg=None)
        self.assertIsInstance(user_objects.join_date, DateTimeField, msg=None)


class TaskTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Set up."""
        Task.objects.create(task_job="task 1 to complete",
                            complete=1,
                            user="User",
                            )
        Task.objects.create(task_job="task 2 to complete",
                            complete=0,
                            user="User",
                            )

    def test_model_fields(self):
        """Test."""
        task_objects = Task.objects.get(task_job="task to complete")
        self.assertIsInstance(task_objects.task_job, TextField, msg=None)
        self.assertIsInstance(task_objects.complete, BooleanField, msg=None)
        self.assertIsInstance(task_objects.email, ForeignKey, msg=None)

"""initialize."""
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    """Migfrations."""

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('task_job', models.TextField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=255)),
                ('last_Name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=200)),
                ('join_date',
                    models.DateTimeField(default=django.utils.timezone.now,
                                         editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_optional',
        ),
        migrations.RemoveField(
            model_name='project',
            name='optional_projects',
        ),
        migrations.AddField(
            model_name='project',
            name='main_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='optional_projects', to='projects.Project'),
        ),
    ]

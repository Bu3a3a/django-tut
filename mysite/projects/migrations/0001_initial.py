# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('help_link', models.URLField(verbose_name='Help link')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('max_mark', models.PositiveIntegerField(default=10, verbose_name='Max mark')),
                ('is_optional', models.BooleanField(default=False, verbose_name='Is optional')),
                ('help_links', models.ManyToManyField(blank=True, to='projects.HelpLink')),
                ('optional_projects', models.ManyToManyField(blank=True, related_name='_project_optional_projects_+', to='projects.Project')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Started at')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='Finished at')),
                ('mark', models.PositiveIntegerField(default=0, verbose_name='Mark')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to='projects.Project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_projects', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

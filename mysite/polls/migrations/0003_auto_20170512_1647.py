# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170510_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(auto_created=datetime.datetime(2017, 5, 12, 16, 47, 49, 785350, tzinfo=utc), verbose_name='Date published'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-08 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180808_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 18, 1, 3, 845261)),
        ),
    ]

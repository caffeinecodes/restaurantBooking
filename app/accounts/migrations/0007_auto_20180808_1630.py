# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-08 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180808_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 16, 30, 45, 704021)),
        ),
    ]

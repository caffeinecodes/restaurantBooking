# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-08 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180808_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 15, 47, 41, 894248)),
        ),
    ]
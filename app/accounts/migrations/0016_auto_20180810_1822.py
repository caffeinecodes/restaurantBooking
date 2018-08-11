# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-10 18:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20180808_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=230, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 18, 22, 35, 668889)),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=230, null=True, verbose_name='last name'),
        ),
    ]

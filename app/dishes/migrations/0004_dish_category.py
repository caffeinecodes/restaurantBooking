# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-08 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_auto_20180808_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dishes.Category'),
            preserve_default=False,
        ),
    ]
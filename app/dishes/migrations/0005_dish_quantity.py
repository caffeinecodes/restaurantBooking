# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-08-10 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_dish_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]

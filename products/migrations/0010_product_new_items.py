# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-11 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180104_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_items',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180103_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]

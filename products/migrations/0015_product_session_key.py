# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20180120_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]

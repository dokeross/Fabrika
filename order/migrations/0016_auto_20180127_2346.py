# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-27 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20180127_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='check_ekb',
            field=models.CharField(default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='check_russia',
            field=models.CharField(default=None, max_length=12, null=True),
        ),
    ]

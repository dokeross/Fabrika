# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-24 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20180224_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcomments',
            name='email',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-16 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20180116_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='image',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-16 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20180116_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='product_image',
            new_name='image',
        ),
    ]

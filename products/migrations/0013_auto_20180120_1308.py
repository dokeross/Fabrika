# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-20 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_liketrue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likeTrue',
            field=models.IntegerField(default=0),
        ),
    ]
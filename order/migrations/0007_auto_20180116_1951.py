# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20180116_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='product_image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-16 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_productinbasket_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='product_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductImage'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-16 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_hit_items'),
        ('order', '0004_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='product_image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductImage'),
        ),
    ]
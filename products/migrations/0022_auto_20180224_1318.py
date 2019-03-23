# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-24 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_product_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comments',
        ),
        migrations.AddField(
            model_name='productcomments',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
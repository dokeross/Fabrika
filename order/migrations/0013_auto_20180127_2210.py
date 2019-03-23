# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-27 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20180127_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_city',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_house',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_index',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_kv',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_street',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
    ]

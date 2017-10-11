# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_remove_stock_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='curr_type',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='supply',
            field=models.PositiveIntegerField(),
        ),
    ]

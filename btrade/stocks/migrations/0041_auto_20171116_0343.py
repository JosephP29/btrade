# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0040_auto_20171116_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyreceipt',
            name='price_bought_at',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sellreceipt',
            name='price_sold_at',
            field=models.FloatField(),
        ),
    ]

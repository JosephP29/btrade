# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0018_remove_user_stock_price_bought_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_stock',
            name='date_sold',
        ),
        migrations.RemoveField(
            model_name='user_stock',
            name='price_sold_at',
        ),
        migrations.RemoveField(
            model_name='user_stock',
            name='sold',
        ),
    ]

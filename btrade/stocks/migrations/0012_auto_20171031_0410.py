# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 04:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0011_buyreceipt_sellreceipt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellreceipt',
            old_name='price_bought_at',
            new_name='price_sold_at',
        ),
    ]

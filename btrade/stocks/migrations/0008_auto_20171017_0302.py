# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_auto_20171017_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_stock',
            old_name='curr_type',
            new_name='stock_curr_type',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0031_auto_20171109_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historystock',
            old_name='curr_type',
            new_name='coin_type',
        ),
        migrations.RenameField(
            model_name='savedstock',
            old_name='curr_type',
            new_name='coin_type',
        ),
        migrations.RenameField(
            model_name='sellreceipt',
            old_name='curr_type',
            new_name='coin_type',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='curr_type',
            new_name='coin_type',
        ),
    ]
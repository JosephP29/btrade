# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 01:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0024_savedstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_stock',
            name='saved',
        ),
    ]

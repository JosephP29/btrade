# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0021_auto_20171105_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_stock',
            name='saved',
            field=models.BooleanField(default=True),
        ),
    ]

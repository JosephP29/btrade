# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0020_historystock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historystock',
            name='curr_type',
            field=models.CharField(max_length=10),
        ),
    ]

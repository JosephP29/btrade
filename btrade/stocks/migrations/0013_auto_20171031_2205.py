# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0012_auto_20171031_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyreceipt',
            name='date_bought',
            field=models.DateTimeField(),
        ),
    ]

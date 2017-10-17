# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 20:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0005_auto_20171010_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('units', models.PositiveIntegerField()),
                ('price_bought_at', models.PositiveIntegerField()),
                ('curr_type', models.CharField(max_length=10, unique=True)),
                ('date_bought', models.DateTimeField()),
                ('sold', models.BooleanField(default=False)),
                ('price_sold_at', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

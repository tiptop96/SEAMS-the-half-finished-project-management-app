# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seams', '0011_auto_20170822_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateField(),
        ),
    ]
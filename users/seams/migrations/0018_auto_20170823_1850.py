# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seams', '0017_auto_20170823_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateField(),
        ),
    ]

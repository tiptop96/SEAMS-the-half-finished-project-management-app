# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seams', '0013_auto_20170822_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default='Add a description of the event!', max_length=250),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seams', '0003_remove_project_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='info',
            field=models.TextField(default='empty'),
        ),
    ]

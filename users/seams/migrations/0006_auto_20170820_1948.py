# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seams', '0005_auto_20170820_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='body',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='internalMeetingCreated',
        ),
        migrations.RemoveField(
            model_name='event',
            name='researchDone',
        ),
        migrations.RemoveField(
            model_name='event',
            name='saleDocLink',
        ),
        migrations.RemoveField(
            model_name='event',
            name='salePointsCreated',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='uniqueTempKey',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='internalMeetingCreated',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='researchDone',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='saleDocLink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='salePointsCreated',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='project',
            name='uniqueTempKey',
            field=models.CharField(default='myNull', max_length=200),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-15 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0009_auto_20160810_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='calendar',
            field=models.URLField(blank=True),
        ),
    ]

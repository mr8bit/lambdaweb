# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-20 20:00
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0010_event_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=django_markdown.models.MarkdownField(),
        ),
    ]

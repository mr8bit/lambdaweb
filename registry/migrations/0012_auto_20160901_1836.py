# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-01 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0011_auto_20160820_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='future',
        ),
        migrations.AlterField(
            model_name='event',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='events/<function get_image_dir_path at 0x7fecf87e4268>'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', django_markdown.models.MarkdownField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(default='https://vk.com/lambdafrela', max_length=100)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('entry_ptr', models.OneToOneField(primary_key=True, to='news.Entry', auto_created=True, parent_link=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=300)),
                ('speaker', models.CharField(blank=True, max_length=100)),
                ('avatar', models.ImageField(null=True, blank=True, upload_to='')),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=('news.entry',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('entry_ptr', models.OneToOneField(primary_key=True, to='news.Entry', auto_created=True, parent_link=True, serialize=False)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', through='taggit.TaggedItem', to='taggit.Tag')),
            ],
            bases=('news.entry',),
        ),
    ]

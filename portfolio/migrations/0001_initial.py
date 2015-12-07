# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('hidden', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'images/')),
                ('thumbnail1', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('thumbnail2', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('hidden', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='images', blank=True, to='portfolio.Category')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]

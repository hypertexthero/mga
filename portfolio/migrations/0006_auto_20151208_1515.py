# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('portfolio', '0005_auto_20151130_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(related_name='images', default=4, blank=True, to='portfolio.Category', null=True),
        ),
    ]

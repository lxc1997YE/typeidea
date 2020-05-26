# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-31 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20200331_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(3, '最热文章'), (2, '最新文章'), (1, 'HTML'), (4, '最近评论')], default=1, verbose_name='展示类型'),
        ),
    ]

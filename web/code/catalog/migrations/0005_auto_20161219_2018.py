# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20161219_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_height',
            field=models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Image Height'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_width',
            field=models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Image Width'),
        ),
    ]

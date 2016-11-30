# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0002_auto_20161118_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True, help_text='This will appear in the customer-facing product listing.', null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='design',
            name='description',
            field=models.TextField(blank=True, help_text='This will appear in the customer-facing product listing.', null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, help_text='This will appear in the customer-facing product listing.', null=True, verbose_name='Description'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20161216_0129'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='color',
            unique_together=set([('code', 'brand')]),
        ),
    ]

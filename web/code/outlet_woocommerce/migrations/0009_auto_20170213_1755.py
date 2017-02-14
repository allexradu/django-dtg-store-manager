# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-13 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlet_woocommerce', '0008_auto_20170213_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpmedia',
            name='is_active',
        ),
        migrations.AddField(
            model_name='wpmediasize',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
    ]
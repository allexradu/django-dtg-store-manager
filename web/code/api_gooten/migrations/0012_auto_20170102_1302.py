# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_gooten', '0011_auto_20170102_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatespace',
            name='final_x1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='templatespace',
            name='final_x2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='templatespace',
            name='final_y1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='templatespace',
            name='final_y2',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20170212_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bzcreativecollection',
            options={'ordering': ['code'], 'verbose_name': 'Creative Collection', 'verbose_name_plural': 'Creative Collections'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativedesign',
            options={'ordering': ['code'], 'verbose_name': 'Creative Design', 'verbose_name_plural': 'Creative Designs'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativelayout',
            options={'ordering': ['code'], 'verbose_name': 'Creative Layout', 'verbose_name_plural': 'Creative Layouts'},
        ),
        migrations.RemoveField(
            model_name='bzcreativelayout',
            name='bzcreativedesign',
        ),
        migrations.AddField(
            model_name='bzcreativelayout',
            name='bzcreativecollection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.bzCreativeCollection', verbose_name='Creative Collection'),
        ),
    ]
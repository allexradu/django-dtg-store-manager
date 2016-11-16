# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web Site')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('agreement', models.TextField(blank=True, default='', null=True, verbose_name='Agreement Notes')),
                ('has_agreement', models.BooleanField(default=False, verbose_name='Agreement in Place?')),
                ('notes', models.TextField(blank=True, default='', null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Artist',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('status', models.CharField(blank=True, choices=[('N', 'New'), ('V', 'In Development'), ('L', 'Live'), ('D', 'Deferred')], default='N', max_length=1, null=True, verbose_name='Status')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creative.Artist')),
            ],
            options={
                'verbose_name': 'Creative',
                'ordering': ['series__code', 'code', 'name'],
                'verbose_name_plural': 'Creative',
            },
        ),
        migrations.CreateModel(
            name='SalesChannel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('web_url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('category', models.CharField(blank=True, choices=[('X', 'Unknown'), ('W', 'Web Shop'), ('M', 'Marketplace'), ('R', 'Retail'), ('L', 'License')], default='X', max_length=1, verbose_name='Category')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Sales Channel',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Sales Channels',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('creative_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creative.Artist', verbose_name='Creative Lead')),
                ('sales_channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creative.SalesChannel', verbose_name='Sales Channel')),
            ],
            options={
                'verbose_name': 'Series',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AddField(
            model_name='creative',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creative.Series'),
        ),
    ]

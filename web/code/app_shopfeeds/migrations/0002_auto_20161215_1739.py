# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_shopfeeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFeed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'DataFeed',
                'ordering': ['name', 'code'],
                'verbose_name_plural': 'DataFeed',
            },
        ),
        migrations.CreateModel(
            name='DataFeedItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=5000, null=True)),
                ('link', models.URLField(blank=True)),
                ('image_link', models.URLField(blank=True)),
                ('availability', models.CharField(blank=True, choices=[('i', 'in stock'), ('o', 'out of stock'), ('p', 'preorder')], default='i', max_length=1, null=True)),
                ('price', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('google_product_category', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('product_type', models.CharField(blank=True, default='', max_length=750, null=True)),
                ('brand', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('mpn', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('condition', models.CharField(blank=True, choices=[('n', 'New'), ('r', 'Refurbished'), ('u', 'Used')], default='', max_length=1, null=True)),
                ('item_group_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('color', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex')], default='', max_length=1, null=True)),
                ('material', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('age_group', models.CharField(blank=True, choices=[('N', 'Newborn'), ('I', 'Infant'), ('T', 'Toddler'), ('K', 'Kids'), ('A', 'Adult')], default='', max_length=1, null=True)),
                ('size', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('shipping_label', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shopfeeds.DataFeed')),
            ],
            options={
                'verbose_name': 'Data Feed Item',
                'ordering': ['feed', 'identifier'],
                'verbose_name_plural': 'Data Feed Items',
            },
        ),
        migrations.DeleteModel(
            name='gCredential',
        ),
    ]
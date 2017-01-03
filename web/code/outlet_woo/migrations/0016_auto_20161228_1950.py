# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outlet_woo', '0015_auto_20161228_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='design',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item_design', to='creative.Design'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_catalog_item', to='catalog.Item'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woo.Shop'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productdefaultattribute',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdefaultattribute',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdefaultattribute',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productdimension',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdimension',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdimension',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productdownload',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdownload',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productdownload',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='code',
            field=models.CharField(blank=True, default='', help_text='', max_length=16, null=True, verbose_name='Code'),
        ),
    ]

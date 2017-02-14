# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_printful', '0007_auto_20170212_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_ca_1',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: Canada, First Item', max_digits=5, verbose_name='CA Ship 1st'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_ca_2',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: Canada, Additional Item', max_digits=5, verbose_name='CA Ship 2nd'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_us_1',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: USA, First Item', max_digits=5, verbose_name='US Ship 1st'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_us_2',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: USA, Additional Item', max_digits=5, verbose_name='US Ship 2nd'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_ww_1',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: Worldwide, First Item', max_digits=5, verbose_name='WW Ship 1st'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='ship_ww_2',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Shipping Rate: Worldwide, Additional Item', max_digits=5, verbose_name='WW Ship 2nd'),
        ),
        migrations.AddField(
            model_name='pfcatalogvariant',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Weight (oz)'),
        ),
        migrations.AlterField(
            model_name='pfcatalogproduct',
            name='is_active',
            field=models.BooleanField(default=True, help_text='', verbose_name='Is Active?'),
        ),
    ]
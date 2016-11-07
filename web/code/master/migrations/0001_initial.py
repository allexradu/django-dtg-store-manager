# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import mptt.fields
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
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Artists',
                'verbose_name': 'Artist',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('image_height', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image_width', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='brand/', verbose_name='Brand Logo', width_field='image_width')),
                ('consumer_url', models.URLField(blank=True, default='', null=True, verbose_name='Consumer URL')),
                ('wholesale_url', models.URLField(blank=True, default='', null=True, verbose_name='Wholesale URL')),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Brands',
                'verbose_name': 'Brand',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=300, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='master.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Name')),
                ('pms_code', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='PMS Code')),
                ('pms_family', models.CharField(blank=True, choices=[('U', 'Uncoated'), ('C', 'Coated'), ('M', 'Metallic'), ('N', 'Neon')], default='', max_length=1, null=True, verbose_name='PMS Family')),
                ('hex_code', models.CharField(blank=True, default='', help_text='The 6-digit hexidecimal code for this colour. Do not include the hash tag.', max_length=64, null=True, verbose_name='HEX Code')),
                ('r_value', models.IntegerField(default=0, help_text='Scale of 0-255', verbose_name='Red Value')),
                ('g_value', models.IntegerField(default=0, help_text='Scale of 0-255', verbose_name='Green Value')),
                ('b_value', models.IntegerField(default=0, help_text='Scale of 0-255', verbose_name='Blue Value')),
            ],
            options={
                'verbose_name_plural': 'Colors',
                'verbose_name': 'Color',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Name')),
                ('note', models.TextField(blank=True, default='', null=True)),
                ('status', models.CharField(blank=True, choices=[('N', 'New'), ('V', 'In Development'), ('L', 'Live'), ('D', 'Deferred')], default='N', max_length=1, null=True, verbose_name='Status')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Artist')),
            ],
            options={
                'verbose_name_plural': 'Creative',
                'verbose_name': 'Creative',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CreativeSeries',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Name')),
                ('note', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Creative Series',
                'verbose_name': 'Creative Series',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GoogleCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Google ID')),
                ('name', models.CharField(blank=True, default='', max_length=300, verbose_name='Google Name')),
                ('long_name', models.CharField(blank=True, default='', max_length=300, verbose_name='Category Name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='master.GoogleCategory')),
            ],
            options={
                'verbose_name_plural': 'Google Product Categories',
                'verbose_name': 'Google Product Category',
            },
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=64, verbose_name='Name')),
                ('web_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('X', 'Unknown'), ('W', 'Web Shop'), ('M', 'Marketplace'), ('R', 'Retail'), ('L', 'License')], default='X', max_length=1, verbose_name='Category')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Outlets',
                'verbose_name': 'Outlet',
            },
        ),
        migrations.CreateModel(
            name='PODVendor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=3, verbose_name='Short Code')),
                ('name', models.CharField(blank=True, default='', max_length=64, verbose_name='Name')),
                ('consumer_url', models.URLField(blank=True, null=True, verbose_name='Consumer URL')),
                ('dashboard_url', models.URLField(blank=True, null=True, verbose_name='Admin Dashboard URL')),
                ('apibase_url', models.URLField(blank=True, null=True, verbose_name='API Base URL')),
                ('api_key', models.CharField(blank=True, default='', max_length=64, verbose_name='API Key')),
                ('api_hash', models.CharField(blank=True, default='', max_length=96, verbose_name='API Hash')),
            ],
            options={
                'verbose_name_plural': 'POD Vendors',
                'verbose_name': 'POD Vendor',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('master_id', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Identifier')),
                ('id_type', models.CharField(choices=[('G', 'GTIN - Global Trade Item Number'), ('M', 'MPN - Manufacturer Part Number')], default='M', max_length=1, verbose_name='ID Type')),
                ('name', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Description')),
                ('link', models.URLField(blank=True, default='', null=True, verbose_name='Product URL')),
                ('mobile_link', models.URLField(blank=True, default='', null=True, verbose_name='Mobile URL')),
                ('image_height', models.CharField(default='0', max_length=10, verbose_name='Image Height')),
                ('image_width', models.CharField(default='0', max_length=10, verbose_name='Image Width')),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='product', verbose_name='Product Image', width_field='image_width')),
                ('additional_image_height', models.CharField(default='0', max_length=10, verbose_name='Additional Image Height')),
                ('additional_image_width', models.CharField(default='0', max_length=10, verbose_name='Additional Image Width')),
                ('additional_image_link', models.ImageField(blank=True, height_field='additional_image_height', null=True, upload_to='product_additional', verbose_name='Additional Image', width_field='additional_image_width')),
                ('is_sellable', models.BooleanField(default=False, verbose_name='Is Sellable Product?')),
                ('age_group', models.CharField(choices=[('N', 'Newborn'), ('I', 'Infant'), ('T', 'Toddler'), ('K', 'Kids'), ('A', 'Adult')], default='A', max_length=1, verbose_name='Age Group')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex')], default='U', max_length=1, verbose_name='Gender')),
                ('material', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Material')),
                ('pattern', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Pattern')),
                ('size_type', models.CharField(blank=True, choices=[('N', 'None'), ('R', 'Regular'), ('T', 'Petite'), ('L', 'Plus'), ('B', 'Big and Tall'), ('M', 'Maternity')], default='N', max_length=1, verbose_name='Size Type')),
                ('size_system', models.CharField(choices=[('US', 'US - United States'), ('UK', 'UK - United Kingdom'), ('EU', 'EU - European Union'), ('DE', 'DE - Germany'), ('FR', 'FR - France'), ('JP', 'JP - Japan'), ('CN', 'CN - China'), ('IT', 'IT - Italy'), ('BR', 'BR - Brazil'), ('MEX', 'MEX - Mexico'), ('AU', 'AU - Australia')], default='US', max_length=3, verbose_name='Size System')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Category')),
                ('googlecategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.GoogleCategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
                'ordering': ['brand', 'master_id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Name')),
                ('sortorder', models.IntegerField(blank=True, default=0, null=True)),
                ('grouping', models.CharField(blank=True, default='', max_length=100, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Sizes',
                'verbose_name': 'Size',
                'ordering': ['grouping', 'sortorder'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Title')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('image_height', models.CharField(default='0', max_length=10, verbose_name='Image Height')),
                ('image_width', models.CharField(default='0', max_length=10, verbose_name='Image Width')),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='product', verbose_name='Product Image', width_field='image_width')),
                ('link', models.URLField(blank=True, default='', null=True, verbose_name='Product URL')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Size')),
            ],
            options={
                'verbose_name_plural': 'Variants',
                'verbose_name': 'Variant',
            },
        ),
        migrations.CreateModel(
            name='VendorBrand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Name')),
                ('vendor_key', models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Vendor ID')),
                ('master_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Brand')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Brands',
                'verbose_name': 'Vendor Brand',
            },
        ),
        migrations.CreateModel(
            name='VendorCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=64, verbose_name='Name')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Categories',
                'verbose_name': 'Vendor Category',
            },
        ),
        migrations.CreateModel(
            name='VendorColor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor ID')),
                ('color_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor Color Code')),
                ('color_group', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor Color Group')),
                ('color_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor Color Name')),
                ('master_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Color')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Colors',
                'verbose_name': 'Vendor Color',
            },
        ),
        migrations.CreateModel(
            name='VendorProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mpn', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Vendor Product MPN')),
                ('sku', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Vendor SKU')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Local Product Name')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Vendor Product Image')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Vendor Description')),
                ('material', models.CharField(blank=True, max_length=128, null=True, verbose_name='Vendor Material')),
                ('country', models.CharField(blank=True, max_length=128, null=True, verbose_name='Vendor Country')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.VendorBrand', verbose_name='Vendor Brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.VendorCategory', verbose_name='Category')),
                ('master_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Product', verbose_name='Master Product')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor', verbose_name='POD Vendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Products',
                'verbose_name': 'Vendor Product',
            },
        ),
        migrations.CreateModel(
            name='VendorSize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor Name')),
                ('vendor_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor ID')),
                ('vendor_grouping', models.CharField(blank=True, default='', max_length=100, verbose_name='Category')),
                ('master_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Size')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor')),
            ],
            options={
                'verbose_name_plural': 'Vendor Sizes',
                'verbose_name': 'Vendor Size',
            },
        ),
        migrations.CreateModel(
            name='VendorVariant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vendor_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='Vendor MPN')),
                ('in_stock', models.BooleanField(default=True)),
                ('price', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Price')),
                ('podvendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.PODVendor')),
                ('vendor_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.VendorColor')),
                ('vendor_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.VendorProduct')),
                ('vendor_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.VendorSize')),
            ],
            options={
                'verbose_name_plural': 'Vendor Variants',
                'verbose_name': 'Vendor Variant',
            },
        ),
        migrations.AddField(
            model_name='creativeseries',
            name='primary_outlet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Outlet'),
        ),
        migrations.AddField(
            model_name='creative',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.CreativeSeries'),
        ),
    ]

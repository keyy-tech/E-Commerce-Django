# Generated by Django 5.1.2 on 2024-10-22 14:16

import Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, default=Products.models.default_image_picture, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default=Products.models.default_image_picture, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default=Products.models.default_image_picture, null=True, upload_to='products/'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]

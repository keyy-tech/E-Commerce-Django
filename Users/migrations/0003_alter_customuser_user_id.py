# Generated by Django 5.1.2 on 2024-10-19 22:54

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_customuser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default=Users.models.generate_unique_user_id, editable=False, max_length=50, unique=True),
        ),
    ]

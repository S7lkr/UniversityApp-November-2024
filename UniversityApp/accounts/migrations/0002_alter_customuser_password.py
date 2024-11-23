# Generated by Django 4.2.16 on 2024-11-20 20:23

import UniversityApp.config.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(4), UniversityApp.config.validators.PasswordValidator()]),
        ),
    ]

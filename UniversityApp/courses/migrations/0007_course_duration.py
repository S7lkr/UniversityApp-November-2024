# Generated by Django 4.2.16 on 2024-11-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_category_alter_course_credits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
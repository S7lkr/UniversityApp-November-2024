# Generated by Django 4.2.16 on 2024-12-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='NoName', max_length=50),
        ),
    ]
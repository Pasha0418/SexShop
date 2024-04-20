# Generated by Django 5.0.2 on 2024-03-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(max_length=160, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(max_length=160, unique=True),
        ),
    ]

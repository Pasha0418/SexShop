# Generated by Django 5.0.2 on 2024-03-15 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_product_height_alter_product_time_work_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='number_product',
            new_name='EAN',
        ),
    ]
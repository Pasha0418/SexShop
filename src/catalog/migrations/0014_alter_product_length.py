# Generated by Django 5.0.2 on 2024-03-15 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_rename_number_product_product_ean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]

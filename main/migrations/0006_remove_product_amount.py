# Generated by Django 4.2.5 on 2023-10-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
    ]

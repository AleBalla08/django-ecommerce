# Generated by Django 3.2.25 on 2025-02-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20250213_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
    ]

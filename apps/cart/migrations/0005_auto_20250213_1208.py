# Generated by Django 3.2.25 on 2025-02-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20250213_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(default='Normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='Credit Card', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]

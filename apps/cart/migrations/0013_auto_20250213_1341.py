# Generated by Django 3.2.25 on 2025-02-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_order_total_price'),
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
    ]

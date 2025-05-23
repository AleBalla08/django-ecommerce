# Generated by Django 3.2.25 on 2025-02-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_auto_20250217_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='delivery_method',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(default='Normal', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='Credit Card', max_length=50),
        ),
    ]

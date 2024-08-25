# Generated by Django 5.1 on 2024-08-25 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_drivers', '0005_alter_deliverydriver_options'),
        ('restaurant_app', '0018_alter_credituser_time_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_order', to='restaurant_app.order'),
        ),
    ]

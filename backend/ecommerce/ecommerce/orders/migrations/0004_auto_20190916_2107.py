# Generated by Django 2.2 on 2019-09-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.DateField(auto_now=True),
        ),
    ]
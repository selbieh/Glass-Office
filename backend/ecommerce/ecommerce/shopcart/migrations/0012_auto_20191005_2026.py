# Generated by Django 2.2 on 2019-10-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0011_auto_20191005_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productobject',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
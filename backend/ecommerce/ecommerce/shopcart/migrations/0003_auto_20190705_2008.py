# Generated by Django 2.2 on 2019-07-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0002_auto_20190623_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='shopCartProduct',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
# Generated by Django 2.2 on 2019-06-22 18:15

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190622_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to=products.models.user_directory_path),
        ),
    ]

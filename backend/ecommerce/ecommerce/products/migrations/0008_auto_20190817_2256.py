# Generated by Django 2.2 on 2019-08-17 20:56

from django.db import migrations
import imagekit.models.fields
import products.utility


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_4',
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=products.utility.user_directory_path_4),
        ),
    ]

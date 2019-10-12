# Generated by Django 2.2 on 2019-10-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190817_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_ar',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(default='lorem', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='note_ar',
            field=models.CharField(blank=True, max_length=130),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
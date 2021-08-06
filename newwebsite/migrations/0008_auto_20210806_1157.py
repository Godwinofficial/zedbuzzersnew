# Generated by Django 3.2.5 on 2021-08-06 11:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newwebsite', '0007_auto_20210806_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-06 21:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newwebsite', '0008_auto_20210806_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ads',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='images'),
        ),
    ]

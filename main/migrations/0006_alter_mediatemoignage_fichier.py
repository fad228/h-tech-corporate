# Generated by Django 5.1.1 on 2025-04-30 15:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_inscription_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediatemoignage',
            name='fichier',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='media'),
        ),
    ]

# Generated by Django 5.1.1 on 2025-04-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_inscription_telephone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]

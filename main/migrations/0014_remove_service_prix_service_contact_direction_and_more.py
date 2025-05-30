# Generated by Django 5.1.1 on 2025-05-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_service_alter_videopublicitaire_fichier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='prix',
        ),
        migrations.AddField(
            model_name='service',
            name='contact_direction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='prix_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='prix_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]

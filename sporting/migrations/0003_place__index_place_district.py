# Generated by Django 5.0.1 on 2024-04-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporting', '0002_place_locality_place_region_sportevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='_index',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

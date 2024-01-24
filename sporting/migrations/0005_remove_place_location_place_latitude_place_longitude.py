# Generated by Django 4.2.7 on 2024-01-01 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporting', '0004_sport_alter_trainer_rewards_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='location',
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
    ]

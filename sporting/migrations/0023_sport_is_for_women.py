# Generated by Django 4.2.7 on 2024-01-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporting', '0022_sport_is_olimpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='is_for_women',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Для женщин'),
        ),
    ]
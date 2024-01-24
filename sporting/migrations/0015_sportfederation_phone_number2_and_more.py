# Generated by Django 4.2.7 on 2024-01-01 14:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sporting', '0014_sportfederation_latitude_sportfederation_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportfederation',
            name='phone_number2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region='RU', verbose_name='Телефон федерации 2'),
        ),
        migrations.AlterField(
            model_name='sportfederation',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region='RU', verbose_name='Телефон федерации'),
        ),
    ]
# Generated by Django 4.2.7 on 2024-01-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sporting', '0017_section_remove_trainer_kind_of_sport_delete_sport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='trainers/djangodbmodelsfieldscharfield'),
        ),
    ]
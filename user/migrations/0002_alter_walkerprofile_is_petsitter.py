# Generated by Django 3.2 on 2022-02-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walkerprofile',
            name='is_petsitter',
            field=models.BooleanField(),
        ),
    ]

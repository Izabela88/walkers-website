# Generated by Django 3.2 on 2022-04-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walker_profile', '0014_auto_20220424_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetails',
            name='is_small_dog',
            field=models.BooleanField(null=True, verbose_name='First Name'),
        ),
    ]

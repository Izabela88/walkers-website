# Generated by Django 3.2 on 2022-03-25 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('walker_profile', '0009_rename_types_servicetypes_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressdetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

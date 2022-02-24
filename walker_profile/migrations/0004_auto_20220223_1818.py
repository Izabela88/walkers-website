# Generated by Django 3.2 on 2022-02-23 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walker_profile', '0003_auto_20220222_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetails',
            name='petsitter_details',
        ),
        migrations.AddField(
            model_name='servicedetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='petsitterdetails',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]

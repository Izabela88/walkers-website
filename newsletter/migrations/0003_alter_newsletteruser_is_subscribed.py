# Generated by Django 3.2 on 2022-03-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_subscribeuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]
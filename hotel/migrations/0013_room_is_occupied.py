# Generated by Django 4.2.1 on 2023-05-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
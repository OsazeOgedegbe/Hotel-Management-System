# Generated by Django 4.2.1 on 2023-05-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]

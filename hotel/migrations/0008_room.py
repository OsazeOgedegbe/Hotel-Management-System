# Generated by Django 4.2.1 on 2023-05-16 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_alter_roomtype_name_alter_roomtype_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-22 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 12, 0, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-26 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0008_auto_20201125_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 11, 26, 17, 7, 30, 969027)),
        ),
    ]
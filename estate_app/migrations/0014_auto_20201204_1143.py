# Generated by Django 3.1.3 on 2020-12-04 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0013_auto_20201203_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='phone_number',
            field=models.IntegerField(default=1234567890),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 4, 11, 43, 34, 435599)),
        ),
        migrations.AlterField(
            model_name='lookingfor',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 4, 11, 43, 34, 443695)),
        ),
    ]
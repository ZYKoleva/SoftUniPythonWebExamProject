# Generated by Django 3.1.3 on 2020-12-12 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0040_auto_20201212_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 12, 20, 34, 51, 590038)),
        ),
        migrations.AlterField(
            model_name='district',
            name='slug',
            field=models.SlugField(),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-22 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0005_auto_20201122_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalfilter',
            old_name='purpose',
            new_name='sale_or_rent',
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 11, 22, 12, 17, 42, 229674)),
        ),
    ]

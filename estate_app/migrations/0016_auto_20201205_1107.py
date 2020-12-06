# Generated by Django 3.1.3 on 2020-12-05 09:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0015_auto_20201204_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 11, 7, 30, 171575)),
        ),
        migrations.AlterField(
            model_name='ad',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.district'),
        ),
        migrations.AlterField(
            model_name='lookingfor',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 11, 7, 30, 171575)),
        ),
    ]
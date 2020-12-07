# Generated by Django 3.1.3 on 2020-12-07 13:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0026_auto_20201205_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='square_meters',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 7, 15, 28, 9, 308386)),
        ),
        migrations.AlterField(
            model_name='additionalfilter',
            name='sort',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estate_app.sortoptions'),
        ),
        migrations.AlterField(
            model_name='lookingfor',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 7, 15, 28, 9, 311640)),
        ),
    ]

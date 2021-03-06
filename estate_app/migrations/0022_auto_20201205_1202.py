# Generated by Django 3.1.3 on 2020-12-05 10:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0021_auto_20201205_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 12, 2, 38, 512546)),
        ),
        migrations.AlterField(
            model_name='ad',
            name='number_rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.numberrooms'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='sale_or_rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.saleorrent'),
        ),
        migrations.AlterField(
            model_name='additionalfilter',
            name='number_rooms',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estate_app.numberrooms'),
        ),
        migrations.AlterField(
            model_name='additionalfilter',
            name='sale_or_rent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estate_app.saleorrent'),
        ),
        migrations.AlterField(
            model_name='lookingfor',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 12, 2, 38, 512546)),
        ),
    ]

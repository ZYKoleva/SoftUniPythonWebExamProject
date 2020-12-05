# Generated by Django 3.1.3 on 2020-12-05 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0024_auto_20201205_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONSTRUCTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ELEVATOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FURNITURE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 12, 37, 41, 987789)),
        ),
        migrations.AlterField(
            model_name='lookingfor',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2020, 12, 5, 12, 37, 41, 987789)),
        ),
        migrations.AlterField(
            model_name='ad',
            name='construction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.construction'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='elevator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.elevator'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='furniture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_app.furniture'),
        ),
    ]

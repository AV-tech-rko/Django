# Generated by Django 3.0.9 on 2020-08-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0013_auto_20200813_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='MyRating',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 2.0.7 on 2020-08-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='Release_year',
            field=models.IntegerField(),
        ),
    ]

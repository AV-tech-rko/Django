# Generated by Django 3.0.9 on 2020-08-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0010_auto_20200807_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='MyRating',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

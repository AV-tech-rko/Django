# Generated by Django 3.0.9 on 2020-08-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0006_ratings_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

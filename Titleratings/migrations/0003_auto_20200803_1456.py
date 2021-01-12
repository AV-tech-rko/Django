# Generated by Django 3.0.9 on 2020-08-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0002_auto_20200803_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='Rating',
            new_name='MyRating',
        ),
        migrations.AddField(
            model_name='ratings',
            name='UserRating',
            field=models.FloatField(blank=True, default=44, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ratings',
            name='Title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
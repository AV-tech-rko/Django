# Generated by Django 3.0.9 on 2020-09-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titleratings', '0022_gameofyear_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='photo',
            field=models.ImageField(default='/staticfiles/images/pending.jpg', upload_to='images/'),
        ),
    ]

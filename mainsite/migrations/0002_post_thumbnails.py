# Generated by Django 3.0.8 on 2020-08-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnails',
            field=models.ImageField(blank=True, default='desktop wallpaper.jpg', null=True, upload_to='images'),
        ),
    ]
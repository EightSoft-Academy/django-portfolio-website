# Generated by Django 3.0.8 on 2020-08-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]

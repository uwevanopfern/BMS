# Generated by Django 2.2.7 on 2020-01-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200125_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]

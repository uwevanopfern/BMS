# Generated by Django 2.2.7 on 2020-01-30 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_billing_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Room'),
        ),
    ]

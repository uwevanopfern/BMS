# Generated by Django 2.2.7 on 2020-01-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_room_is_occupied'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.CharField(max_length=100, unique=True)),
                ('client_phone', models.CharField(max_length=100)),
                ('client_address', models.CharField(max_length=100)),
                ('payment_time', models.CharField(max_length=200)),
                ('reminder_days', models.IntegerField()),
                ('business_desc', models.TextField()),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Room')),
            ],
        ),
    ]

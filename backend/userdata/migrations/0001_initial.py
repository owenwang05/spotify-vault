# Generated by Django 5.0.6 on 2024-06-09 04:11

import datetime
import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('snapshot_cached', models.BooleanField(default=False)),
                ('last_saved', models.DateTimeField(default=datetime.date(1, 1, 1), verbose_name='Last Saved')),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date Saved')),
                ('username', models.CharField(default='null', max_length=30)),
                ('avatar_url', models.CharField(default='', max_length=100)),
                ('listening_time', models.IntegerField(default=0)),
                ('top_genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=list, size=5)),
                ('top_songs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=list, size=5)),
                ('top_artists', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=list, size=5)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.profile')),
            ],
        ),
    ]

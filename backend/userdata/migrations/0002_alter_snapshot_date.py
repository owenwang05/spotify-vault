# Generated by Django 5.0.6 on 2024-06-09 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Saved'),
        ),
    ]
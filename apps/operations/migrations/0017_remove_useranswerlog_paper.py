# Generated by Django 2.1.4 on 2021-04-24 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0016_auto_20210331_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswerlog',
            name='paper',
        ),
    ]
# Generated by Django 2.1.4 on 2021-04-27 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0017_remove_useranswerlog_paper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='status',
        ),
    ]

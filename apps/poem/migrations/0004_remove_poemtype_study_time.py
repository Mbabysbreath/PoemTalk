# Generated by Django 2.1.4 on 2021-03-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0003_remove_poem_study_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poemtype',
            name='study_time',
        ),
    ]

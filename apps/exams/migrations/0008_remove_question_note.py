# Generated by Django 2.1.4 on 2021-06-12 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20210612_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='note',
        ),
    ]

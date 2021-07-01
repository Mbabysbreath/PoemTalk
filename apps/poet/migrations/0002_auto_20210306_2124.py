# Generated by Django 2.1.4 on 2021-03-06 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poetinfo',
            name='poem_style',
        ),
        migrations.AddField(
            model_name='poetinfo',
            name='desc',
            field=models.TextField(default=' ', verbose_name='诗人简介'),
        ),
        migrations.AddField(
            model_name='poetinfo',
            name='story',
            field=models.TextField(default=' ', verbose_name='生平故事'),
        ),
    ]

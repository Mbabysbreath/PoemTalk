# Generated by Django 2.1.4 on 2021-03-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0003_remove_poetinfo_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='poetinfo',
            name='love_num',
            field=models.IntegerField(default=0, verbose_name='收藏数'),
        ),
    ]

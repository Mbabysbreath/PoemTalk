# Generated by Django 2.1.4 on 2021-06-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0024_delete_usermessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlove',
            name='love_type',
            field=models.IntegerField(choices=[(1, '题目'), (2, '诗词'), (3, '诗人')], verbose_name='收藏类别'),
        ),
    ]

# Generated by Django 2.1.4 on 2021-05-31 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0022_auto_20210531_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercollection',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usercollection',
            name='question',
        ),
        migrations.RemoveField(
            model_name='usercollection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userrecord',
            name='course',
        ),
        migrations.RemoveField(
            model_name='userrecord',
            name='question',
        ),
        migrations.RemoveField(
            model_name='userrecord',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserCollection',
        ),
        migrations.DeleteModel(
            name='UserRecord',
        ),
    ]

# Generated by Django 2.1.4 on 2021-02-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20210201_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='用户生日'),
        ),
    ]

# Generated by Django 2.1.4 on 2021-03-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_ans',
            field=models.TextField(default='', null=True, verbose_name='用户答案'),
        ),
    ]

# Generated by Django 2.1.4 on 2021-06-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0013_auto_20210614_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionType',
            field=models.CharField(choices=[('xz', '选择题'), ('judgment', '判断题')], default='single_choice', max_length=20, verbose_name='题目类型'),
        ),
    ]

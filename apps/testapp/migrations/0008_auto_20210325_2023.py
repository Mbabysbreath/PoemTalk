# Generated by Django 2.1.4 on 2021-03-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_question_user_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user_ans',
            field=models.TextField(default=' ', verbose_name='用户答案'),
        ),
    ]

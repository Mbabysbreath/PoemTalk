# Generated by Django 2.1.4 on 2021-02-22 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_remove_question_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paperlist',
            name='multiple_choice_num',
        ),
        migrations.RemoveField(
            model_name='paperlist',
            name='multiple_choice_score',
        ),
    ]
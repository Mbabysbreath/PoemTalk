# Generated by Django 2.1.4 on 2021-03-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0010_usercomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='comment_content',
            field=models.TextField(default='', max_length=300, verbose_name='评论内容'),
        ),
    ]

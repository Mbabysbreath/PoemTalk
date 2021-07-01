# Generated by Django 2.1.4 on 2021-06-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '诗词鉴赏管理',
                'verbose_name_plural': '诗词鉴赏管理',
            },
        ),
    ]
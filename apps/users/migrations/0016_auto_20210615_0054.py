# Generated by Django 2.1.4 on 2021-06-15 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_delete_bannerinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifycode',
            name='send_type',
            field=models.IntegerField(choices=[(1, '注册账号'), (2, '修改密码'), (3, '修改邮箱')], verbose_name='验证码类型'),
        ),
    ]

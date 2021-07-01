# Generated by Django 2.1.4 on 2021-03-02 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_auto_20210302_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercomment',
            options={'verbose_name': '评论管理', 'verbose_name_plural': '评论管理'},
        ),
        migrations.AddField(
            model_name='usercomment',
            name='comment_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.ArticleModel', verbose_name='评论帖子'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment_content',
            field=models.TextField(max_length=300, verbose_name='评论内容'),
        ),
    ]

# Generated by Django 2.1.4 on 2021-03-02 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0008_auto_20210302_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='comment_poem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poem.Poem', verbose_name='评论诗词'),
        ),
    ]
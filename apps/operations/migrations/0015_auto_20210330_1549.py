# Generated by Django 2.1.4 on 2021-03-30 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0014_auto_20210326_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_paper',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testapp.CourseList', verbose_name='所属课程'),
        ),
        migrations.AlterField(
            model_name='create_paper',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.PaperList', verbose_name='试卷名称'),
        ),
        migrations.AlterField(
            model_name='useranswerlog',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.CourseList', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='useranswerlog',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Paper', verbose_name='试卷'),
        ),
        migrations.AlterField(
            model_name='usercollection',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.CourseList', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='usercollection',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Question', verbose_name='题目'),
        ),
        migrations.AlterField(
            model_name='userrecord',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.CourseList', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='userrecord',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Question', verbose_name='题目'),
        ),
    ]
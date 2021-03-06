# Generated by Django 2.1.4 on 2021-06-14 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20210612_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='decs',
            field=models.CharField(default='', max_length=500, verbose_name='诗词类别说明'),
        ),
        migrations.AlterField(
            model_name='courselist',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='诗词类别'),
        ),
        migrations.AlterField(
            model_name='paperlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.CourseList', verbose_name='所属诗词类别'),
        ),
    ]

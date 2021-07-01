from django.db import models
from datetime import datetime

from django.utils import timezone

from poet.models import PoetInfo
# Create your models here.
class PoemType(models.Model):
    image = models.ImageField(upload_to='poem/',max_length=200,verbose_name='诗词种类封面')
    name = models.CharField(max_length=20,verbose_name='诗词种类名称')
    study_num = models.IntegerField(default=0,verbose_name='学习人数')
    desc=models.CharField(max_length=200,verbose_name="诗词种类简介")
    detail = models.TextField(verbose_name="诗词种类详情",default="")
    is_banner = models.BooleanField(default=False,verbose_name="是否轮播")
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="诗词种类信息"
        verbose_name_plural=verbose_name

'''
具体种类下的诗词：
1.诗词名称
2.视频/音频
3.文本内容
4.诗词种类和诗词：一对多
5.收藏数
6.访问量，学习人数

'''
class Poem(models.Model):
    name = models.CharField(max_length=50,verbose_name='诗词名称')
    contents = models.TextField(verbose_name='诗词内容')
    author = models.CharField(max_length=10,verbose_name='作者')
    translation = models.TextField(verbose_name='译文',default=' ')
    note = models.TextField(verbose_name='注释',default=' ')
    url = models.CharField(default='暂无音频资源',verbose_name='音频链接',max_length=200)
    poemtype = models.ForeignKey(PoemType,verbose_name='所属诗词种类',on_delete=models.CASCADE)
    love_num=models.IntegerField(default=0,verbose_name='收藏数')
    click_num=models.IntegerField(default=0,verbose_name='访问量')
    study_num = models.IntegerField(default=0, verbose_name='学习人数')
    poetinfo=models.ForeignKey(PoetInfo,verbose_name='所属作者',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now,verbose_name='添加时间')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='诗词信息'
        verbose_name_plural=verbose_name






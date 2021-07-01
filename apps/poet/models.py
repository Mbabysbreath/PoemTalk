from django.db import models
# Create your models here.
from django.utils.html import format_html

'''诗人信息：
1.诗人头像
2.诗人名字
3.朝代
4.诗词风格
5.外键：一种类别的诗词，由很多诗人
'''
class PoetInfo(models.Model):
    image = models.ImageField(upload_to='poet/',max_length=200,verbose_name='作者头像')
    name = models.CharField(max_length=20,verbose_name='作者姓名')
    address = models.CharField(max_length=20,verbose_name='所属朝代')
    desc = models.TextField(verbose_name='诗人简介',default=" ")
    love_num=models.IntegerField(default=0,verbose_name='收藏数')

    def image_data(self):
        return format_html(
            '<img src="{}" width="30px"/>',
            self.image.url,
        )

    image_data.short_description = u'诗人头像'




    def __str__(self):
        return self.name
    class Meta:
        verbose_name='诗人信息'
        verbose_name_plural=verbose_name


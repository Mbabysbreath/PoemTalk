from django.db import models

# Create your models here.
class PoemModel(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    content=models.TextField(verbose_name='内容')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '诗词鉴赏管理'
        verbose_name_plural = verbose_name


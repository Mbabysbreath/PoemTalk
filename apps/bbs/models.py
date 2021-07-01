from django.db import models

# Create your models here.
class CategoryModel(models.Model):

    name=models.CharField(max_length=20,unique=True,verbose_name='分类名')


    # 和Admin相关
    def __str__(self):
        return self.name

    # 修改表选项
    class Meta:
        # 和Admin后台相关
        verbose_name='分类管理'
        verbose_name_plural=verbose_name


class ArticleModel(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    content=models.TextField(verbose_name='内容')
    category=models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True,verbose_name='分类')
    user=models.ForeignKey('users.UserProfile',on_delete=models.SET_NULL,null=True,verbose_name='用户')
    publish_time=models.DateTimeField(auto_now_add=True,verbose_name='发布日期')
    read_count=models.IntegerField(default=0,verbose_name='阅读量')
    comments = models.IntegerField(default=0,verbose_name='评论量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 用户表
class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='user/',max_length=200,verbose_name='用户头像',null=True,blank=True)
    nick_name=models.CharField(max_length=20,verbose_name='用户昵称',null=True,blank=True,default="童生")
    gender = models.CharField(choices=(('girl','女'),('boy','男')),max_length=10,verbose_name='用户性别',default='girl')
    # 这个字段控制激活
    is_start = models.BooleanField(default=False,verbose_name='是否激活')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    def __str__(self):
        return self.username
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name


# 邮箱验证码表

class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20,verbose_name='邮箱验证码')
    email = models.EmailField(max_length=200,verbose_name='验证码邮箱')
    send_type = models.IntegerField(choices=((1,'注册账号'),(2,'修改密码'),(3,'修改邮箱')),verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码信息'
        verbose_name_plural = verbose_name
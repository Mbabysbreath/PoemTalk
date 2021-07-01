from django.db import models
from datetime import datetime
from users.models import UserProfile
from poem.models import Poem,PoetInfo
from bbs.models import ArticleModel
from exams.models import CourseList,Question,PaperList
from users.models import UserProfile
# Create your models here.


'''用户收藏表：
1.收藏者
2.收藏id
3.收藏种类
4.收藏状态
'''
class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile,verbose_name='收藏用户',on_delete=models.CASCADE)
# 用id,type表示所有收藏的东西
    love_id = models.IntegerField(verbose_name='收藏id')
    love_type = models.IntegerField(choices=((1,'题目'),(2,'诗词'),(3,'诗人')),verbose_name='收藏类别')
    love_poet = models.CharField(max_length=50,verbose_name='收藏诗人',default='')
    love_poem = models.CharField(max_length=50,verbose_name='收藏诗词',default='')
    love_status = models.BooleanField(default=False,verbose_name='收藏状态')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='收藏时间')

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name='收藏信息'
        verbose_name_plural=verbose_name

class UserPoem(models.Model):
    study_man = models.ForeignKey(UserProfile,verbose_name='学习用户',on_delete=models.CASCADE)
    study_poem = models.ForeignKey(Poem,verbose_name='学习诗词',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='学习时间')

    def __str__(self):
        return self.study_man.username
    class Meta:
        # 一名用户学过同一首之后，就不要再次添加学习记录了，所以保持联合唯一
        unique_together = ('study_man','study_poem')
        verbose_name='用户学习诗词信息'
        verbose_name_plural=verbose_name


'''用户评论的信息'''
class UserComment(models.Model):
    comment_man = models.ForeignKey(UserProfile, verbose_name='评论用户',on_delete=models.CASCADE)
    comment_poem = models.ForeignKey(Poem, verbose_name='评论诗词',on_delete=models.CASCADE,null=True)
    comment_content = models.TextField(max_length=300,verbose_name='评论内容',default='')
    comment_article=models.ForeignKey(ArticleModel,verbose_name='评论帖子',on_delete=models.CASCADE,null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        verbose_name='评论管理'
        verbose_name_plural=verbose_name
'''
用户收到的消息：
1.消息接收者
2.消息内容
3.消息阅读状态'''
# class UserMessage(models.Model):
#     # 0 --系统消息  其他--对应的用户
#     message_man = models.IntegerField(default=0,verbose_name='消息用户')
#     message_content = models.CharField(max_length=200,verbose_name='消息内容')
#     message_staut = models.BooleanField(default=False,verbose_name='消息状态')
#     add_time = models.DateTimeField(default=datetime.now,verbose_name='消息时间')
#
#     def __str__(self):
#         return self.message_content
#     class Meta:
#         verbose_name='用户消息信息'
#         verbose_name_plural=verbose_name





class PaperCache(models.Model):#随机考试题目存储位置
    question = models.IntegerField(verbose_name=u"题目")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.CASCADE)
    class Meta:
        verbose_name = u"试题临时列表"
        verbose_name_plural = verbose_name



class UserAnswerLog(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.CASCADE)
    course = models.ForeignKey(CourseList, verbose_name=u"课程",on_delete=models.CASCADE)
    # paper = models.ForeignKey(Paper,verbose_name=u"试卷",on_delete=models.CASCADE)
    paper_name = models.CharField(max_length=20,verbose_name=u"试卷名称",default="")
    # answer = models.TextField(verbose_name=u"用户答案")
    score = models.IntegerField(verbose_name=u"得分")
    add_time = models.DateField(default=datetime.now, verbose_name=u"作答时间")

    class Meta:
        verbose_name = u"用户做题记录"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.paper_name
    # def __unicode__(self):
    #     return "{0}({1}) score={2}".format(self.user.nick_name,self.user.id,self.score)


# class UserCollection(models.Model):#刷题模式下收藏了哪些题目
#     user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.CASCADE)
#     course = models.ForeignKey(CourseList, verbose_name=u"课程",on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, verbose_name=u"题目",on_delete=models.CASCADE)
#     add_time = models.DateField(verbose_name=u"录入时间",default=datetime.now)


# class UserRecord(models.Model):#刷题模式下记录到哪一个题目
#     user = models.ForeignKey(UserProfile, verbose_name=u"用户",on_delete=models.CASCADE)
#     course = models.ForeignKey(CourseList, verbose_name=u"课程",on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, verbose_name=u"题目",on_delete=models.CASCADE)
#     add_time = models.DateField(verbose_name=u"录入时间",default=datetime.now)



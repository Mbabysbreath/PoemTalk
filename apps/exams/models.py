from django.db import models
from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.

# 测试的诗词类别范围
class CourseList(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"诗词类别", default="")
    decs = models.CharField(max_length=500, verbose_name=u"诗词类别说明", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:#模型的元数据，指的是“除了字段外的所有内容”，例如排序方式、数据库表名、人类可读的单数或者复数名等等。
        verbose_name = u"测试范围"  #模型数据名称
        verbose_name_plural = verbose_name   #复数名称
    def __str__(self):
        return self.name

# 题目
class Question(models.Model):
    course = models.ForeignKey(CourseList, verbose_name=u"考试科目",on_delete=models.CASCADE)
    questionType = models.CharField(max_length=20, choices=(("xz", u"选择题"), ("judgment", u"判断题")), default="single_choice", verbose_name=u"题目类型")
    content = models.TextField(verbose_name=u"题目内容")
    answer = models.TextField(verbose_name=u"正确答案")
    user_ans=models.TextField(verbose_name=u"用户答案",default="暂无",null=True)
    choice_a = models.TextField(verbose_name=u"A选项", default="A.")
    choice_b = models.TextField(verbose_name=u"B选项", default="B.")
    choice_c = models.TextField(verbose_name=u"C选项", default="C.")
    choice_d = models.TextField(verbose_name=u"D选项", default="D.")
    boolt = models.TextField(verbose_name=u"判断正误正确选项", default= "对")
    boolf = models.TextField(verbose_name=u"判断正误错误选项", default= "错")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    choice_num = models.IntegerField(verbose_name=u"选项数", default=4)

    class Meta:
        verbose_name = "题库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content



# 测试试卷
class PaperList(models.Model):
    course = models.ForeignKey(CourseList, verbose_name=u"所属诗词类别",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"试卷名", default=u"")
    is_allow = models.BooleanField(default=False, verbose_name=u"启用随机组卷")
    add_time = models.DateField(default=datetime.now, verbose_name=u"开考时间")
    single_choice_num = models.IntegerField(verbose_name=u"单选题数", default=0)
    single_choice_score = models.IntegerField(verbose_name=u"单选分值", default=0)
    judgment = models.IntegerField(verbose_name=u"判断题数", default=0)
    judgment_score = models.IntegerField(verbose_name=u"判断分值", default=0)
    random_paper = models.BooleanField(default=True, verbose_name=u"随机卷")

    class Meta:
        verbose_name = u"试卷列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

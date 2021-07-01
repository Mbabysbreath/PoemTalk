# # import xadmin
# # from .models import *
# # # Create your models here.
# # # 古诗词测试管理
# # '''
# # 1.题目的诗词种类
# # 2.每一类的封面
# # '''
# # class PoemTestXadmin(object):
# #     list_display=['poem_type','image','add_time']
# #     model_icon = 'fa fa-trophy' # 设置对应模块的图标
# #
# #     # poem_type = models.CharField(max_length=10,verbose_name='题目种类')
# #     # # poem_type = models.CharField(choices=(('ts','唐诗'),('sc','宋词'),('ly','论语'),('yf','乐府')))
# #     # image = models.ImageField(upload_to='testapp/',max_length=200,verbose_name='诗词封面')
# #     # add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')
# #     #
# #     # def __str__(self):
# #     #     return self.poem_type
# #     # class Meta:
# #     #     verbose_name = '题目种类'
# #     #     verbose_name_plural = verbose_name
# #
# # '''
# #  题目信息：
# #  1.题干内容
# #  2.题目答案
# #  3.分值
# #  4.外键：一类诗词下面多个题目
# # '''
# # class PoemInfoXadmin(object):
# #     list_display = ['poem_text','answer','value','poemtest']
# #     model_icon = 'fa fa-quora'
# #
# # '''诗人信息：
# # 1.诗人头像
# # 2.诗人名字
# # 3.朝代
# # 4.诗词风格
# # 5.外键：一种类别的诗词，由很多诗人
# # '''
# # class PoetInfoXadmin(object):
# #     list_display=['image','name','address','poem_style','poemtest']
# #     model_icon = 'fa fa-user-circle'
# # xadmin.site.register(PoemTest,PoemTestXadmin)
# # xadmin.site.register(PoemInfo,PoemInfoXadmin)
# # xadmin.site.register(PoetInfo,PoetInfoXadmin)
#
# import xadmin
# from xadmin import views
# from .models import CourseList,Question, Paper,PaperList
#
#
# class CourseListAdmin(object):
#     list_display = ['name', 'decs', 'add_time']
#     search_fields = ['name', 'decs']
#     list_filter = ['name', 'decs', 'add_time']
#
# class QuestionAdmin(object):
#     list_display = ['course','questionType',  'content', 'answer', 'choice_a', 'choice_b',
#                     'choice_c', 'choice_d', 'note', 'boolt', 'boolf', 'add_time']
#     search_fields = ['course','questionType', 'content', 'answer', 'choice_a', 'choice_b',
#                      'choice_c', 'choice_d', 'note', 'boolt', 'boolf']
#     list_filter = ['course__name','questionType',  'content', 'answer', 'choice_a',
#                    'choice_b', 'choice_c', 'choice_d', 'note', 'boolt', 'boolf','add_time']
#
# class PaperListAdmin(object):
#     list_display = ['id','course','name', 'is_allow', 'add_time']
#     search_fields = ['id','course', 'name', 'is_allow']
#     list_filter = ['id','course__name','name', 'is_allow', 'add_time']
#
# class PaperAdmin(object):
#     list_display = ['course', 'paper_name', 'question', 'add_time']
#     search_fields = ['course', 'paper_name__name', 'paper_name__id', 'paper_name__is_allow', 'question__id',
#                      'question__content', 'question__answer']
#     list_filter = ['course__name', 'paper_name', 'question__id', 'question__content','add_time','paper_name__name',]
#
# xadmin.site.register(CourseList, CourseListAdmin)
# xadmin.site.register(Question, QuestionAdmin)
# xadmin.site.register(PaperList, PaperListAdmin)
# xadmin.site.register(Paper, PaperAdmin)

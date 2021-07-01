import xadmin
from .models import *
from xadmin import views
from .models import UserAnswerLog
# Create your models here.


class UserAskXadmin(object):
    list_display = ['poem_name','poet_name','conent']
    model_icon = 'fa fa-american-sign-language-interpreting'

class UserLoveXadmin(object):
    list_display = ['love_man','love_id','love_type','love_status']
    model_icon = 'fa fa-gratipay'

#     love_man = models.ForeignKey(UserProfile,verbose_name='收藏用户',on_delete=models.CASCADE)
# # 用id,type表示所有收藏的东西
#     love_id = models.IntegerField(verbose_name='收藏id')
#     love_type = models.IntegerField(choices=((1,'problems'),(2,'poem'),(3,'poet')),verbose_name='收藏类别')
#     love_status = models.BooleanField(default=False,verbose_name='收藏状态')
#     add_time=models.DateTimeField(default=datetime.now,verbose_name='收藏时间')


class UserPoemXadmin(object):
    list_display=['study_man','study_poem']
    model_icon = 'fa fa-linode'
    # study_man = models.ForeignKey(UserProfile,verbose_name='学习用户',on_delete=models.CASCADE)
    # study_poem = models.ForeignKey(Poem,verbose_name='学习诗词',on_delete=models.CASCADE)
    # add_time = models.DateTimeField(default=datetime.now,verbose_name='学习时间')


class UserCommentXadmin(object):
    list_display=['comment_man','comment_poem','comment_content','add_time']
    model_icon = 'fa fa-commenting-o'



class UserMessageXadmin(object):
    # 0 --系统消息  其他--对应的用户
    list_display = ['message_man','message_content','message_staut','add_time']
    model_icon = 'fa fa-bell-o'





class UserAnswerLogAdmin(object):
    list_display = ['user', 'paper', 'answer','score', 'add_time']
    search_fields = ['user__nick_name', 'user__username', 'paper__paper_name', 'answer', 'score']
    list_filter = ['user', 'paper', 'answer', 'score', 'add_time']


class UserScoreAdmin(object):
    list_display = ['user', 'paper', 'total', 'add_time']
    search_fields = ['user__nick_name', 'user__username', 'paper__paper_name', 'total']
    list_filter = ['user', 'paper', 'total','add_time']


xadmin.site.register(UserAnswerLog, UserAnswerLogAdmin)
xadmin.site.register(UserComment,UserCommentXadmin)
# xadmin.site.register(UserAsk,UserAskXadmin)
xadmin.site.register(UserLove,UserLoveXadmin)
# xadmin.site.register(UserMessage,UserMessageXadmin)
xadmin.site.register(UserPoem,UserPoemXadmin)

import xadmin
from .models import *
class PoemTypeXadmin(object):
    list_display = ['image','name','study_time','study_num']
    list_editable=['image','name','study_time','study_num']
    # style_fields = {'detail':'ueditor'}


'''
具体种类下的诗词：
1.诗词名称
2.视频/音频
3.文本内容
4.诗词种类和诗词：一对多
5.资源下载（可选）
'''
class PoemXadmin(object):
    list_display=['name','contents','author','poemtype']
    model_icon = 'fa fa-file-text'
    # name = models.CharField(max_length=50,verbose_name='诗词名称')
    # contents = models.CharField(max_length=50,verbose_name='诗词内容')
    # author = models.CharField(max_length=10,verbose_name='作者')
    # video = models.CharField(max_length=50,verbose_name='视频/音频内容')
    # url = models.URLField(default='http://www.atfuigu.com',verbose_name='视频链接',max_length=200)
    # poemtype = models.ForeignKey(PoemType,verbose_name='所属诗词种类',on_delete=models.CASCADE)
    # down_lode = models.FileField(upload_to='source/',verbose_name='资源下载',max_length=200)
    # add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
xadmin.site.register(PoemType, PoemTypeXadmin)
xadmin.site.register(Poem,PoemXadmin)


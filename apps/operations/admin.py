from django.contrib import admin
from .models import *
class UserAnswerLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'paper_name','score', 'add_time']
    # search_fields = ['user__nick_name', 'user__username', 'paper__paper_name']
    list_filter = ['user', 'paper_name']
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['comment_man','comment_poem','comment_article','comment_content']
    list_filter = ['comment_man', 'comment_poem','comment_article']
class UserLoveAdmin(admin.ModelAdmin):
    list_display = ['love_man', 'love_type','love_poem','love_poet']
    list_filter = ['love_man', 'love_type','love_poem','love_poet']
class UserPoemAdmin(admin.ModelAdmin):
    list_display = ['study_man','study_poem']
    list_filter = ['study_man','study_poem']
# Register your models here.
admin.site.register(UserAnswerLog,UserAnswerLogAdmin)
admin.site.register(UserComment,UserCommentAdmin)
admin.site.register(UserLove,UserLoveAdmin)
admin.site.register(UserPoem,UserPoemAdmin)

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# from .models import CourseList,Question, Paper,PaperList
from .models import CourseList,Question,PaperList

class CourseListAdmin(admin.ModelAdmin):
    list_display = ['name', 'decs', 'add_time']
    list_filter = ['name', 'add_time']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course','questionType',  'content', 'answer']
    list_filter = ['course__name','questionType',  'content']



admin.site.register(CourseList,CourseListAdmin)
admin.site.register(Question,QuestionAdmin)

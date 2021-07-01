from django.contrib import admin
from .models import *


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title','user','category','read_count']
    list_filter = ['title','user','category']
# Register your models here.
admin.site.register(ArticleModel,ArticleModelAdmin)
admin.site.register(CategoryModel)
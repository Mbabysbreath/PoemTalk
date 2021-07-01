from django.contrib import admin
from .models import *
# Register your models here.
class PoetInfoAdmin(admin.ModelAdmin):
    list_display = ['name','image_data','address','love_num']
    list_filter = ['name']
admin.site.register(PoetInfo,PoetInfoAdmin)
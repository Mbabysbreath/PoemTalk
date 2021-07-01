from django.contrib import admin

# Register your models here.

from .models import *
class PoemTypeAdmin(admin.ModelAdmin):
    list_display = ['name','is_banner','study_num']
    list_filter=['name']

class PoemAdmin(admin.ModelAdmin):
    list_display=['name','author','poemtype']
    list_filter = ['name','author','poemtype']

admin.site.register(PoemType,PoemTypeAdmin)
admin.site.register(Poem,PoemAdmin)


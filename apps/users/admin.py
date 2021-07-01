from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username','nick_name','is_start','is_staff']
    list_filter = ['username','nick_name']
class EmailVerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['email','code','send_type']
    list_filter = ['email','send_type']
# Register your models here.

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(EmailVerifyCode,EmailVerifyCodeAdmin)
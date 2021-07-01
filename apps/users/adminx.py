import xadmin
from .models import EmailVerifyCode
from xadmin import views # 注册主题app 使用专用的view注册


# 配置主题--界面无显示，不报错
class BaseXadminSetting(object):
    enable_themes =True
    use_bootswatch  = True

# 设置全局外观
class CommXadminSetting(object):
    site_title = '诗 说'
    site_footer = '基于Python的古诗词学习系统'
    menu_style = 'accordion' # 设置模块下拉菜单

# 轮播图表
class BannerInfoXadmin(object):
    list_display = ['image','url','add_time']
    search_fields = ['image', 'url'] #添加搜索轮播图信息的框框
    list_filter=['image','url']# 添加过滤器
# 邮箱验证码表
class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email','send_type','add_time']


# xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)#注册主题
# 注册全局样式类
xadmin.site.register(views.CommAdminView,CommXadminSetting)
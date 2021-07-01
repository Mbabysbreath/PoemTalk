"""PoemTalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from .views import history
from django.conf.urls import url
from .views import user_love,user_deletelove,user_comment
app_name = 'operations'
urlpatterns = [
    path('history/', history , name="history"),
    url(r'^user_love/$',user_love,name='user_love'),
    url(r'^user_deletelove/$',user_deletelove,name='user_deletelove'),
    url(r'^user_comment/$', user_comment, name='user_comment'),

]

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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import poem_search,poem_list,poem_detail,poem_study,poem_content,poem_comment
urlpatterns = [
    url(r'^poem_list/$',poem_list,name="poem_list"),
    url(r'^poem_detail/(\d+)/$',poem_detail,name='poem_detail'),
    url(r'poem_study/(\d+)/$',poem_study,name='poem_study'),
    url(r'poem_content/(\d+)/$',poem_content,name='poem_content'),
    url(r'^poem_comment/(\d+)/$', poem_comment, name='poem_comment'),
    url(r'^poem_search/$',poem_search,name='poem_search')

]

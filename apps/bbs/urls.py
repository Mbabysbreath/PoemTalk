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
from django.urls import path
from django.conf.urls import url
from .views import BBSIndexView,artical_list,PublishView,DetailView,ReplyView
app_name = 'bbs'
urlpatterns = [
    url(r'^BBSIndexView/$', BBSIndexView.as_view(), name='BBSIndexView'),
    url(r'^artical_list/(\d+)$' ,artical_list,name='artical_list'),
    url(r'^detail/(\d+)$',DetailView.as_view(),name='detail'),
    url(r'^publish$',PublishView.as_view(),name='publish'),
    # path('detail/<int:id>/',DetailView.as_view(),name='detail'),
    path('reply/',ReplyView.as_view(),name='reply'),

]

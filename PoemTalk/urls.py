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
from django.urls import path
from django.conf.urls import url,include
from users.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^captcha/', include('captcha.urls')),
    path('users/',include(('users.urls','users'),namespace='users')),
    path('poem/',include(('poem.urls','poem'),namespace='poem')),
    path('poet/',include(('poet.urls','poet'),namespace='poet')),
    path('exams/',include(('exams.urls','exams'),namespace='exams')),
    path('operations/',include(('operations.urls','operations'),namespace='operations')),
    path('bbs/',include(('bbs.urls','bbs'),namespace='bbs')),

]
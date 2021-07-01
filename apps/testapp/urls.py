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

from django.conf.urls import url
    # po_detail
from django.urls import path,include,re_path
from .views import po_test,PaperListView,PaperView
app_name = 'testapp'
urlpatterns = [
    url(r'po_test/$',po_test,name='po_test'),
#试卷列表
    path("paperlist/", PaperListView.as_view(),name='paperlist'),
    path('paper/<paper_id>/', PaperView.as_view(), name="paper"),
    # url(r'^paper/(?P<paper_id>[0-9])+/$', PaperView.as_view(), name="paper")
]

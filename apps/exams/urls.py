from django.urls import path,include,re_path
from .views import po_test,PaperListView,PaperView

from django.conf.urls import url
app_name = 'Exams'

urlpatterns = [
    #试卷列表
    url(r'po_test/$', po_test, name='po_test'),
    path("paperlist/", PaperListView.as_view(),name='paperlist'),
    path('paper/<paper_id>/', PaperView.as_view(), name="paper"),

]
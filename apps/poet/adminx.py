import xadmin
from .models import *
class PoetInfoXadmin(object):
    list_display = ['image', 'name', 'address', 'poem_style']
    model_icon = 'fa fa-user-circle'




xadmin.site.register(PoetInfo, PoetInfoXadmin)
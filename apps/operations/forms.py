from django import forms
# from .models import UserAsk
import re


class UserCommentForm(forms.Form):
    poem = forms.IntegerField(required=True)
    content = forms.CharField(required=True,min_length=1,max_length=300)



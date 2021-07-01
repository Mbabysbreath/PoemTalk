from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile, EmailVerifyCode


class UserRegisterForm(forms.Form):
    #EmailField会用邮箱规则进行验证
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6,max_length=15,error_messages={
        'required':'密码不能为空',
        'min_length':'密码长度至少6位',
        'max_length':'密码不超过15位'

    })
    captcha = CaptchaField()

class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6,max_length=15,error_messages={
        'required':'密码不能为空',
        'min_length':'密码长度至少6位',
        'max_length':'密码不超过15位'

    })

class UserForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

class UserResetForm(forms.Form):
    password = forms.CharField(required=True,min_length=6,max_length=15,error_messages={
        'required':'密码必须填写',
        'min_length':'密码至少6位',
        'max_length':'密码不能超过15位'
    })
    password1 = forms.CharField(required=True,min_length=6,max_length=15,error_messages={
        'required':'密码必须填写',
        'min_length':'密码至少6位',
        'max_length':'密码不能超过15位'
    })
# 使用ModelForm做修改
class UserChaneImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender']

class UserChangeEmailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']

class UserResetEmailForm(forms.ModelForm):
    class Meta:
        model = EmailVerifyCode
        fields = ['email','code']
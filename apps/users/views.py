from django.shortcuts import render,redirect,reverse
from .forms import UserResetEmailForm,UserChangeEmailForm,UserChangeInfoForm,UserChaneImageForm,UserRegisterForm,UserLoginForm,UserForgetForm,UserResetForm
from .models import UserProfile,EmailVerifyCode
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from tools.send_mail_tool import send_email_code
from django.http import JsonResponse
from datetime import datetime
from operations.models import UserLove
from poem.models import Poem,PoemType
from poet.models import PoetInfo
from django.views.generic import View
# Create your views here.
# 首页
class IndexView(View):
    def get(self,request):
        banner_poemtype = PoemType.objects.filter(is_banner=True)
        all_poemtype = PoemType.objects.filter(is_banner=False).order_by('-study_num')[:6]
        all_poets = PoetInfo.objects.order_by('-love_num')[:15]
        return render(request, 'index.html', {
            'banner_poemtype': banner_poemtype,
            'all_poemtype': all_poemtype,
            'all_poet': all_poets
        })

    def post(self, request):
        pass

# 注册页面
class UserRegisterView(View):
    def get(self,request):
        user_register_form = UserRegisterForm()
        return render(request, 'register.html', {
            'user_register_form': user_register_form
        })
        # 这里实例化forms类，目的不是为了验证，而是为了使用验证码
    def post(self, request):
        user_register_form=UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            user_list = UserProfile.objects.filter(Q(username=email)|Q(email=email))
            if user_list:
                return render(request,'register.html',{
                    'msg':'用户已经存在'
                })
            else:
                a=UserProfile()
                a.username=email
                a.set_password(password)
                a.email=email
                a.save()
                send_email_code(email,1)
                return  render(request,'register.html',{
                    'msg':'邮箱激活链接已发送，请尽快激活'
                })
        else:
            return render(request,'register.html',{
                'user_register_form':user_register_form,
                'msg':'获取注册表单出错'
            })

# 登录页面
class UserLoginView(View):
    def get(self,request):
        user_login_form=UserLoginForm()
        return render(request, 'login.html',{
            'user_login_form':user_login_form
        })

    def post(self,request):
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']
            print("email==",email)
            print("pwd==",password)
            # 验证
            user = authenticate(username=email, password=password)
            print("是否可以通过认证==",user)
            if user:
                if user.is_start:
                    login(request, user)
                    #获取url，有可能是登录后跳转到之前的访问页面
                    url=request.COOKIES.get('url','/')
                    ret = redirect(url)
                    #每次重新访问后，把上一次的cookie删除
                    ret.delete_cookie('url')
                    # return redirect(reverse('index'))
                    return  ret
                else:
                    return render(request,'login.html',{
                        'msg':'请先激活邮箱，否则无法登录'
                    })

            else:
                return render(request, 'login.html', {
                    'msg': '邮箱或密码有误'
                })
        else:
            return render(request, 'login.html', {
                'user_login_form': user_login_form,
                'msg': '邮箱或密码有误'
            })

# 退出页面
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
#激活邮箱
def user_active(request,code):
    if code:
        print("===code:",code)
        email_ver_list=EmailVerifyCode.objects.filter(code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            email=email_ver.email
            user_list=UserProfile.objects.filter(username=email)
            if user_list:
                user=user_list[0]
                user.is_start=True
                user.save()
                print("===reverse解析地址：",reverse('users:user_login'))
                return redirect(reverse('users:user_login'))
            else:
                pass
        else:
            pass
    else:
        pass
# 忘记密码
def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request,'forgetpwd.html',{
            'user_forget_form':user_forget_form
        })
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                send_email_code(email,2)
                return render(request,'forgetpwd.html',
                              {'msg':'链接已发送，请尽快前往邮箱去重置密码'
                })
            else:
                return render(request,'forgetpwd.html',{
                    'msg':'用户不存在',
                    'user_forget_form':user_forget_form
                })
        else:
            return render(request, 'forgetpwd.html', {
                'user_forget_form': user_forget_form
            })
# 修改密码
def user_reset(request,code):
    if code:
        if request.method == 'GET':
            return render(request,'password_reset.html',{
                'code':code
            })
        else:
            user_reset_form = UserResetForm(request.POST)
            if user_reset_form.is_valid():
                password = user_reset_form.cleaned_data['password']
                password1 = user_reset_form.cleaned_data['password1']
                if password == password1:
                    email_ver_list = EmailVerifyCode.objects.filter(code=code)
                    if email_ver_list:
                        email_ver = email_ver_list[0]
                        email = email_ver.email
                        user_list = UserProfile.objects.filter(email=email)
                        if user_list:
                            user = user_list[0]
                            user.set_password(password1)
                            user.save()
                            return redirect(reverse('users:user_login'))
                        else:
                            pass
                    else:
                        pass
                else:
                    return render(request,'password_reset.html',{
                        'msg':'两次密码不一致',
                        'code':code
                    })
            else:
                return render(request, 'password_reset.html', {
                    'user_reset_form': user_reset_form,
                    'code': code
                })
#修改密码
def user_resetpwd(request):
    user_reset_form = UserResetForm(request.POST)
    if user_reset_form.is_valid():
        password = user_reset_form.cleaned_data['password']
        password1 = user_reset_form.cleaned_data['password1']
        print("pwd=",password)
        print("pwd1=",password1)
        if password == password1:
                user=request.user
                user.set_password(password1)
                user.save()
                return JsonResponse({"status":'ok',"msg":'修改成功'})

        else:
            return JsonResponse({'status': 'false','msg':'修改失败，请保持密码前后一致'})
    else:
        return JsonResponse({'status': 'false', 'msg': '修改失败，请检查密码格式，密码长度要求6-15位'})
# 个人中心
def user_info(request):
    return render(request,'users/usercenter-info.html')

#修改头像,instance=request.user代表修改的实例是当前用户实例
def user_changeimage(request):
    #instance指明实例是什么，做修改的时候，我们需要知道是给那个对象实例进行修改
    # 如果不指明，那么就会被当做创建对象去执行
    user_changeimage_form = UserChaneImageForm(request.POST,request.FILES,instance=request.user)
    if user_changeimage_form.is_valid():
        user_changeimage_form.save(commit=True)
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status': 'false'})

def user_changeinfo(request):
    user_changeinfo_form=UserChangeInfoForm(request.POST,instance=request.user)
    print("user_info=",user_changeinfo_form)
    if user_changeinfo_form.is_valid():
        user_changeinfo_form.save(commit=True)
        return JsonResponse({"status":'ok',"msg":'修改成功'})
    else:
        return JsonResponse({"status":'false',"msg":'修改失败'})

#修改邮箱-获取验证码
def user_changeemail(request):
    '''
    当用户修改邮箱，点击获取验证码的时候，会通过这个函数处理，发送邮箱验证码
    :param request: http请求对象
    :return: 返回json数据，在模板页面当中去处理
    '''
    user_changeemail_form = UserChangeEmailForm(request.POST)
    if user_changeemail_form.is_valid():
        email = user_changeemail_form.cleaned_data['email']
        user_list = UserProfile.objects.filter(Q(email=email)|Q(username=email))
        if user_list:
            return JsonResponse({'status':'false','msg':'该邮箱已经被绑定,请输入其他邮箱'})
        else:
            #我们在发送邮箱验证码之前，应该去邮箱验证码的表当中去查找，看之前有没有往当前这个邮箱发送过修改邮箱这个类型的验证码
            email_ver_list = EmailVerifyCode.objects.filter(email=email,send_type=3)
            #如果发送过验证码，那么我们就拿到最近发送的这一个
            if email_ver_list:
                email_ver = email_ver_list.order_by('-add_time')[0]
            #判断当前时间和最近发送的验证码添加时间之差
                if (datetime.now()-email_ver.add_time).seconds > 60:
                    #如果我们重新发送了新的验证码，那么以前最近发的就被清了
                    send_email_code(email,3)
                    email_ver.delete()
                    return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱当中获取验证码'})
                else:
                    return JsonResponse({'status': 'false', 'msg': '请不要重复发送验证码，1分钟后重试'})
            else:
                send_email_code(email, 3)
                return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱当中获取验证码'})
    else:
        return JsonResponse({'status': 'false', 'msg': '您的邮箱有问题'})
# 重置邮箱
def user_resetemail(request):
    user_resetemail_form = UserResetEmailForm(request.POST)
    if user_resetemail_form.is_valid():
        email = user_resetemail_form.cleaned_data['email']
        code = user_resetemail_form.cleaned_data['code']
        email_ver_list = EmailVerifyCode.objects.filter(email=email,code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            if (datetime.now() - email_ver.add_time).seconds < 60:
                request.user.username = email
                request.user.email = email
                request.user.save()
                return JsonResponse({'status':'ok','msg':'邮箱修改成功'})
            else:
                return JsonResponse({'status': 'false', 'msg': '验证码失效，请重新发送验证码'})
        else:
            return JsonResponse({'status': 'false', 'msg': '邮箱或者验证码有误,请仔细检查'})
    else:
        return JsonResponse({'status': 'false', 'msg': '邮箱或者验证码不合法'})

def user_lovepoet(request):
    userlovepoet_list = UserLove.objects.filter(love_man=request.user, love_type=3, love_status=True)
    poet_ids = [userlovepoet.love_id for userlovepoet in userlovepoet_list]
    poet_list = PoetInfo.objects.filter(id__in=poet_ids)
    no_poet = '空空如也~~'
    if poet_list:
        return render(request, 'users/usercenter-fav-poet.html', {
            'poet_list': poet_list
        })
    else:
        return render(request, 'users/usercenter-fav-poet.html', {
            'no_poet':no_poet
        })
def user_lovepoem(request):
    userlovepoem_list = UserLove.objects.filter(love_man=request.user,love_type=2,love_status=True)
    poem_ids = [userlovepoem.love_id for userlovepoem in userlovepoem_list]
    poem_list = Poem.objects.filter(id__in=poem_ids)
    no_poem = '空空如也~~'
    if poem_list:
        return render(request,'users/usercenter-fav-poem.html',{
            'poem_list':poem_list
        })
    else:
        return render(request, 'users/usercenter-fav-poem.html', {
             'no_poem':no_poem
        })


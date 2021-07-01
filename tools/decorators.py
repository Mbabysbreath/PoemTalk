from django.shortcuts import redirect,reverse
from django.http import JsonResponse

def login_decorator(func):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'status':'nologin'})
            # 不同请求之间想要保持状态用session或cookie
            #拿到目前访问的完整url，不只是路径部分
            url = request.get_full_path()
            print("目前完整的url:",url)
            ret = redirect(reverse('users:user_login'))
            ret.set_cookie('url',url)
            return ret
    return inner

# f1 = login_decorator(f1)
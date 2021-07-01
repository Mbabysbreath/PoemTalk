from users.models import EmailVerifyCode
from random import randrange
from django.core.mail import send_mail
from PoemTalk.settings import EMAIL_FROM
# 生成验证码
def get_random_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code=''
    for i in range(code_length):
        # 随机选择一个字符。code+=该字符
        # code += choice(code_source)
        str = code_source[randrange(0,len(code_source)-1)]
        code+=str
    return code

# 创建随机验证码
def send_email_code(email,send_type):
    # 1.创建邮箱验证码对象，保存数据库，用来以后和用户输入做对比
    code = get_random_code(6)
    a = EmailVerifyCode()
    a.email=email
    a.send_type=send_type
    a.code =code
    a.save()
    # 2正式发邮件功能
    send_title = ''
    send_body=''
    if send_type == 1:
        send_title="欢迎注册-诗说"
        send_body='请点击以下链接进行账号激活：\n '
        # code='cjmr7w'
        send_body+="http://127.0.0.1:8000/users/user_active/"
        # send_body+=mail_msg
        send_body+=code
        send_mail(send_title,send_body,EMAIL_FROM,[email])
    if send_type == 2:
        send_title = "诗说-修改密码操作"
        send_body = '请点击以下链接进行密码修改：\n '
        # code='cjmr7w'
        send_body += "http://127.0.0.1:8000/users/user_reset/"
        # send_body+=mail_msg
        send_body += code
        send_mail(send_title, send_body, EMAIL_FROM, [email])
    if send_type == 3:
            send_title = "诗说-修改邮箱验证码"
            send_body = '您的验证码是：\n '+code
            send_mail(send_title, send_body, EMAIL_FROM, [email])

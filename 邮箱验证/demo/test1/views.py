import hashlib
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.


from django.contrib.auth.hashers import make_password, check_password

def demo1(request):
    pwd = make_password('123456', salt='sdasas')
    print(pwd)

    pwd2 = check_password('123456', 'pbkdf2_sha256$100000$sdasas$1sb9+D6RhcgU5VtiDcQkcWVBM2I7F40BmPypKERT2Ow=')
    print(pwd2)
    return HttpResponse()


def arrive_register_form(request):
    """
    访问注册表单
    :param request: 无
    :return: 响应到注册表单
    """
    return render(request, 'register.html')


def hash_code(s, salt='oracle'):
    """
    hashcode 方法
    :param s:
    :param salt:
    :return:
    """
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def make_confirm_string(user):
    """
    为用户生成唯一的验证码
    :param user: 用户对象
    :return:生成完成的验证码
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.username, now)
    models.ConfirmedString.objects.create(code=code, user=user)

    return code


def send_email(email, code):
    subject, from_email, to = '来自的测试邮件', '18500230996@sina.cn', email,
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8000', code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_register(request):
    """
    真正处理注册逻辑的view
    :param request: 需要获取用户输入的表单参数
    :return:处理完成的数据以及模板
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    new_user = models.TUser.objects.create(username=username, password=password, email=email)
    code = make_confirm_string(new_user)
    send_email(email, code)
    return render(request, 'login.html')


def user_confirm_email(request):
    """
    验证从邮箱超链接发送的请求
    :param request:生成code
    :return:返回验证的结果
    """
    code = request.GET.get('code')
    try:
        confirm = models.ConfirmedString.objects.get(code=code)
    except:
        message = '无效的请求'
        return render(request, 'register.html')

    confirm.user.has_confirmed = True
    confirm.user.save()
    confirm.delete()
    message = '感谢验证，您可以登录了'
    return render(request, 'login.html', locals())

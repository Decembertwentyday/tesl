from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import pymysql
from django.views.generic import View
from personal_page.models import *
from main_body.models import *
import re

user = User


# def search_(request):
#     if 'user_name' not in request.session:
# return render(request,'login.html')
# user_name=request.session['user_name']
# user=User.objects.filter(user_name=user_name)
# if user:
# user=user[0]
# keyword=request.GET.get('keyword')

# if not keyword:
# error_msg='请输入关键字'
# return render(request,'index.html',{'errmsg':'没找到你需要的信息','error_msg':error_msg})
#
# else:

# return render(request,'index.html'key)


def login_(request):
    if request.method == 'POST':

        user = User.objects.get(user_name=request.POST.get('user_name'))

        if user.pwd != request.POST.get('pwd'):
            return render(request, 'login.html', {'errmsg': '用户密码不正确'})

        elif user.user_name != request.POST.get('user_name'):
            return render(request, 'login.html', {'errmsg': '用户名不存在'})

        elif user is None:
            return render(request, 'login.html', {'errmsg': '输入错误'})

        else:
            # login(request,user)
            print("1")
            user_name = request.POST.get('user_name')
            return render(request, 'index.html', {'name': user_name})
    else:
        return render(request, 'login.html')


def logout_(request):
    if 'user_name' in request.session:
        del request.session['user_name']
        travels = TravelNotes.objects.filter().order_by('-likenum')
        travels01 = travels[0]
        travels02 = travels[1]
        travels03 = travels[2]
        travels04 = travels[3]
        travels_shi = TravelNotes.objects.filter(source='食在人间').order_by('-likenum')
        travels_shi01 = travels_shi[0]
        travels_shi02 = travels_shi[1]
        travels_shi03 = travels_shi[2]
        travels_shi04 = travels_shi[3]
        travels_you = TravelNotes.objects.filter(source='旅游胜地').order_by('-likenum')
        travels_you01 = travels_you[0]
        travels_you02 = travels_you[1]
        travels_you03 = travels_you[2]
        travels_you04 = travels_you[3]
        travels_gou = TravelNotes.objects.filter(source='购物天堂').order_by('-likenum')
        travels_gou01 = travels_gou[0]
        travels_gou02 = travels_gou[1]
        travels_gou03 = travels_gou[2]
        travels_gou04 = travels_gou[3]
        travels_feng = TravelNotes.objects.filter(source='自然风光').order_by('-likenum')
        travels_feng01 = travels_feng[0]
        travels_feng02 = travels_feng[1]
        travels_feng03 = travels_feng[2]
        travels_feng04 = travels_feng[3]
        travels_min = TravelNotes.objects.filter(source='民俗体味').order_by('-likenum')
        travels_min01 = travels_min[0]
        travels_min02 = travels_min[1]
        travels_min03 = travels_min[2]
        travels_min04 = travels_min[3]
        travels_tian = TravelNotes.objects.filter(classes='天津').order_by('-likenum')
        travels_tian01 = travels_tian[0]
        travels_tian02 = travels_tian[1]
        travels_tian03 = travels_tian[2]
        travels_tian04 = travels_tian[3]
        travels_hai = TravelNotes.objects.filter(classes='海南').order_by('-likenum')
        travels_hai01 = travels_hai[0]
        travels_hai02 = travels_hai[1]
        travels_hai03 = travels_hai[2]
        travels_hai04 = travels_hai[3]
        travels_shan = TravelNotes.objects.filter(classes='山东').order_by('-likenum')
        travels_shan01 = travels_shan[0]
        travels_shan02 = travels_shan[1]
        travels_shan03 = travels_shan[2]
        travels_shan04 = travels_shan[3]
        travels_he = TravelNotes.objects.filter(classes='河南').order_by('-likenum')
        travels_he01 = travels_he[0]
        travels_he02 = travels_he[1]
        travels_he03 = travels_he[2]
        travels_he04 = travels_he[3]
        travels_shanxi = TravelNotes.objects.filter(classes='陕西').order_by('-likenum')
        travels_shanxi01 = travels_shanxi[0]
        travels_shanxi02 = travels_shanxi[1]
        travels_shanxi03 = travels_shanxi[2]
        travels_shanxi04 = travels_shanxi[3]
        return render(request,'index.html',locals())
    else:
        travels = TravelNotes.objects.filter().order_by('-likenum')
        travels01 = travels[0]
        travels02 = travels[1]
        travels03 = travels[2]
        travels04 = travels[3]
        travels_shi = TravelNotes.objects.filter(source='食在人间').order_by('-likenum')
        travels_shi01 = travels_shi[0]
        travels_shi02 = travels_shi[1]
        travels_shi03 = travels_shi[2]
        travels_shi04 = travels_shi[3]
        travels_you = TravelNotes.objects.filter(source='旅游胜地').order_by('-likenum')
        travels_you01 = travels_you[0]
        travels_you02 = travels_you[1]
        travels_you03 = travels_you[2]
        travels_you04 = travels_you[3]
        travels_gou = TravelNotes.objects.filter(source='购物天堂').order_by('-likenum')
        travels_gou01 = travels_gou[0]
        travels_gou02 = travels_gou[1]
        travels_gou03 = travels_gou[2]
        travels_gou04 = travels_gou[3]
        travels_feng = TravelNotes.objects.filter(source='自然风光').order_by('-likenum')
        travels_feng01 = travels_feng[0]
        travels_feng02 = travels_feng[1]
        travels_feng03 = travels_feng[2]
        travels_feng04 = travels_feng[3]
        travels_min = TravelNotes.objects.filter(source='民俗体味').order_by('-likenum')
        travels_min01 = travels_min[0]
        travels_min02 = travels_min[1]
        travels_min03 = travels_min[2]
        travels_min04 = travels_min[3]
        travels_tian = TravelNotes.objects.filter(classes='天津').order_by('-likenum')
        travels_tian01 = travels_tian[0]
        travels_tian02 = travels_tian[1]
        travels_tian03 = travels_tian[2]
        travels_tian04 = travels_tian[3]
        travels_hai = TravelNotes.objects.filter(classes='海南').order_by('-likenum')
        travels_hai01 = travels_hai[0]
        travels_hai02 = travels_hai[1]
        travels_hai03 = travels_hai[2]
        travels_hai04 = travels_hai[3]
        travels_shan = TravelNotes.objects.filter(classes='山东').order_by('-likenum')
        travels_shan01 = travels_shan[0]
        travels_shan02 = travels_shan[1]
        travels_shan03 = travels_shan[2]
        travels_shan04 = travels_shan[3]
        travels_he = TravelNotes.objects.filter(classes='河南').order_by('-likenum')
        travels_he01 = travels_he[0]
        travels_he02 = travels_he[1]
        travels_he03 = travels_he[2]
        travels_he04 = travels_he[3]
        travels_shanxi = TravelNotes.objects.filter(classes='陕西').order_by('-likenum')
        travels_shanxi01 = travels_shanxi[0]
        travels_shanxi02 = travels_shanxi[1]
        travels_shanxi03 = travels_shanxi[2]
        travels_shanxi04 = travels_shanxi[3]
        return render(request,'index.html',locals())


def register_(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        user_email = request.POST.get('user_email')
        allow = request.POST.get('allow')

        if not all([user_name, pwd, user_email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', user_email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        user = User(user_name=user_name, user_email=user_email, pwd=pwd)

        user.save()
        return render(request, 'login.html')


def index_(request):
    travels = TravelNotes.objects.filter().order_by('-likenum')
    travels01 = travels[0]
    travels02 = travels[1]
    travels03 = travels[2]
    travels04 = travels[3]
    travels_shi = TravelNotes.objects.filter(source='食在人间').order_by('-likenum')
    travels_shi01 = travels_shi[0]
    travels_shi02 = travels_shi[1]
    travels_shi03 = travels_shi[2]
    travels_shi04 = travels_shi[3]
    travels_you = TravelNotes.objects.filter(source='旅游胜地').order_by('-likenum')
    travels_you01 = travels_you[0]
    travels_you02 = travels_you[1]
    travels_you03 = travels_you[2]
    travels_you04 = travels_you[3]
    travels_gou = TravelNotes.objects.filter(source='购物天堂').order_by('-likenum')
    travels_gou01 = travels_gou[0]
    travels_gou02 = travels_gou[1]
    travels_gou03 = travels_gou[2]
    travels_gou04 = travels_gou[3]
    travels_feng = TravelNotes.objects.filter(source='自然风光').order_by('-likenum')
    travels_feng01 = travels_feng[0]
    travels_feng02 = travels_feng[1]
    travels_feng03 = travels_feng[2]
    travels_feng04 = travels_feng[3]
    travels_min = TravelNotes.objects.filter(source='民俗体味').order_by('-likenum')
    travels_min01 = travels_min[0]
    travels_min02 = travels_min[1]
    travels_min03 = travels_min[2]
    travels_min04 = travels_min[3]
    travels_tian = TravelNotes.objects.filter(classes='天津').order_by('-likenum')
    travels_tian01 = travels_tian[0]
    travels_tian02 = travels_tian[1]
    travels_tian03 = travels_tian[2]
    travels_tian04 = travels_tian[3]
    travels_hai = TravelNotes.objects.filter(classes='海南').order_by('-likenum')
    travels_hai01 = travels_hai[0]
    travels_hai02 = travels_hai[1]
    travels_hai03 = travels_hai[2]
    travels_hai04 = travels_hai[3]
    travels_shan = TravelNotes.objects.filter(classes='山东').order_by('-likenum')
    travels_shan01 = travels_shan[0]
    travels_shan02 = travels_shan[1]
    travels_shan03 = travels_shan[2]
    travels_shan04 = travels_shan[3]
    travels_he = TravelNotes.objects.filter(classes='河南').order_by('-likenum')
    travels_he01 = travels_he[0]
    travels_he02 = travels_he[1]
    travels_he03 = travels_he[2]
    travels_he04 = travels_he[3]
    travels_shanxi = TravelNotes.objects.filter(classes='陕西').order_by('-likenum')
    travels_shanxi01 = travels_shanxi[0]
    travels_shanxi02 = travels_shanxi[1]
    travels_shanxi03 = travels_shanxi[2]
    travels_shanxi04 = travels_shanxi[3]

    if 'user_name' not in request.session:

        if request.method == 'POST':
            user_name = request.POST.get('user_name')

            pwd = request.POST.get('pwd')

            try:
                user = User.objects.get(user_name=user_name)
            except:
                return render(request, 'login.html', {'errmsg': '用户名不存在'})

            if user.pwd == pwd:
                # 用户名或者密码正确
                request.session['user_name'] = user_name

                return render(request, 'index.html', locals())
            else:
                return render(request, 'login.html', {'errmsg': '用户密码错误'})

        return render(request, 'index.html',locals())

    if 'user_name' in request.session:
        user_name = request.session['user_name']
        return render(request, 'index.html', locals())

def search(request):
    print(2)
    if 'user_name' not in request.session:
        return render(request,'login.html')
    user_name=request.session['user_name']
    user=User.objects.get(user_name=user_name)
    if request.method == 'POST':
        # user=user[0]
        keyword = request.POST.get('keyword', '')
        print(1)
        if not keyword:
            error_msg = '请输入关键字'
            return render(request, 'index.html', locals())
        else:
            print(3)
            p = TravelNotes.objects.filter(title__contains='%s' % keyword)
            if not p:
                print(4)
                # return render(request,'register.html')
                return render(request, 'search.html', {'errmsg': '抱歉没找到您想要的..'})
            else:
                return render(request, 'search.html', locals())
            # return HttpResponse("hahah")


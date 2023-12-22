from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def login_(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        checkbox = request.POST.get('checkbox')
        user_ = authenticate(username=username, password=password)
        if not user_:
            return HttpResponse('用户名或密码错误')
        else:
            request.session['id'] = user_.id
            login(request, user_)
            if not checkbox:
                request.session.set_expiry(0)
            return HttpResponseRedirect('/')


def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        gender = request.POST.get('gender')
        phone_number = request.POST['phoneNumber']
        institute = request.POST['institute']
        try:
            user_ = UserInfo.objects.create_user(username=username, password=password, email=email, phone_number=phone_number, work_place=institute, gender=gender)
            request.session['id'] = user_.id
            login(request, user_)
        except Exception as e:
            print('error%s' % e)
            HttpResponse('注册失败！请联系管理人员')
        print("zhuce")
        return HttpResponseRedirect('/')

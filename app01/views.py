from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import json


# Create your views here.

def home (request):
    dic = {'name': 'liyang', 'age': '18', 'user_list': ['shuai', 'ge', 'hen', 'shuai'], }
    list = map(str ,range(100))
    return render(request,'home.html',{'list':list})

def son(request):
    return render(request,'son.html')

def index(request):

    dic = {}
    from app01 import models
    if request.method == 'POST':
        email = request.POST['em']
        pwd = request.POST['pw']
        #创建数据
        models.UserInfo.objects.create(email = email,pwd = pwd )
        dic['status'] = '添加成功'

    #查询所有数据
    user_info_list = models.UserInfo.objects.all()
    dic['user_info_list'] = user_info_list
    return render(request,'index.html',dic)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if email == 'nyzplym@sina.com' and pwd == 'liyang':
            return redirect('/index/')
    else:
        return render(request, 'login.html',{'status':'用户名或密码错误'})
    return render(request,'login.html')

def delU(request):
    from app01 import models
    if request.method == 'POST':
        em = request.POST['em']
        models.UserInfo.objects.filter(email =em).delete()
        return HttpResponse(json.dumps({'status':'true'}))
    return render(request,'index.html')

def add2(request,a ,b):
    return HttpResponse(str(int(a)+int(b)))
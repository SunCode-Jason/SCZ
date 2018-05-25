from django.shortcuts import render,redirect
from SCZ_Web.models import SCZ_User
from  django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def login(requset):
    if requset.method == 'GET':
        return render(requset,'Base/login.html')
    else:
        post = requset.POST
        account = post.get("account", '')
        password = post.get('password', '')
        if len(SCZ_User.objects.all()) <= 0 :
            user = SCZ_User()
            user.LoginName='Admin'
            user.Password=make_password('SCZ_Admin')
            user.RealName='James'
            user.CreateUser='SCZ'
            user.save()
        user = SCZ_User.objects.filter(LoginName=account)
        if len(user) > 0:
            if check_password(password,user[0].Password):
                return redirect("/index")
            else:
               return render(requset,'Base/login.html',{'errormessage': '密码错误！'})
        else:
            return  render(requset,'Base/login.html',{'errormessage': '用户名不存在！'})



def index(requset):
    return render(requset,'Base/index.html')

def home(request):
    return render(request,'Base/homes.html')
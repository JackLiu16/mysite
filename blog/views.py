#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import Article


# Create your views here.

def index(request):
    return render(request,"index.html")
#@login_required
def movie(request):
    return render(request,"movie.html")
#@login_required
def edindex(request):
    Articles = Article.objects.all()
    #print type(Articles)    
    return render(request,"edindex.html",{"Articles":Articles})



#@login_required
def mod(request):
    articles = Article.objects.all()  
    return render(request,"mod.html",{'articles':articles})



#@login_required
def articlelist(request,article_id): 
    #articles = Article.objects.all()  
    article = Article.objects.get(pk=article_id)
    return render(request,"articlelist.html",{'article':article})

#@login_required
def articleforeword(request):
    #articles = Article.objects.all()  
    return render(request,"articleforeword.html")



@login_required
def modtool(request):
    return render(request,"modtool.html")

@login_required
def echart1(request):
    return render(request,"echarts1.html")

@login_required
def echart2(request):
    return render(request,"echarts2.html")

@login_required
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username # 将session 信息记录到浏览器
            response = HttpResponseRedirect('modtool/')
            return response
        else:
            return render(request,'index.html', {'error': 'username or password error!'})
    else:
        return render(request,'index.html', {'error': 'username or password error!'})

#@login_required
def event_manage(request):
    username = request.session.get('user', '') # 读取浏览器cookie
    #return render(request,"event_manage.html",{"user":username,"Articles":Article})
    return render(request,"event_manage.html",{"user":username})
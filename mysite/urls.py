#coding=utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ckeditor/', include(ckeditor.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^logout/$', views.index), 
    url(r'^mod/logout/$', views.index),
    url(r'^event_manage/logout/$', views.index),
    url(r'^accounts/login/$', views.index),   
    url(r'^admin/', views.index),


    url(r'^mod/$', views.mod),
    url(r'^modtool/$', views.modtool),
    url(r'^login_action/modtool/$', views.modtool),
    url(r'^edindex', views.edindex),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^movie/$',views.movie,name="movie"),
    url(r'^articlelist/(?P<article_id>[0-9]+)$', views.articlelist,name='articlelist'),
    url(r'^articleforeword/$',views.articleforeword),


    url(r'^echart1/$', views.echart1), 
    url(r'^echart2/$', views.echart2), 
]

#urlpatterns += staticfiles_urlpatterns()

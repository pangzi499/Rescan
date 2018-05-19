#encoding:utf-8
"""Rescan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin  
from Rescan import view as st 
#调用view里面的函数
from django.contrib.auth.views import login
#urlpatterns在url文件中是一个url映射列表
urlpatterns = [

    url(r'^$', st.index),#url和后台函数的绑定
    url(r'^index', st.index,name='index'),
    url(r'^poc_list$', st.poc_list,name='poc_list'),
    url(r'^about$', st.about,name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^history',st.xhistory,name='history')
]

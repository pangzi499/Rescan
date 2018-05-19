# coding:utf-8
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from zero import models
import os

def index(request):
    
    modelss_ = ""
    mode_ = ""
    url = ""
    context1 = ""
    context2 = ""
    context = {}
    if request.POST:
        modelss_ = request.POST['cars']
    if request.POST:
        url = request.POST['text']
        context1 = u"目标地址:%s\n"%url + u"[*] 任务开始......\t\n" 

    if modelss_ == "1":
        url_ = u"http://" + url
        context2 = os.popen("java -jar D:\\temp\\Rescan\\PocList\\verify_CVE-2017-12149.jar %s"%url_)
        x = context2.read().decode('utf-8')
        if len(x) <= 30:
            print x
            a = u"[*]目标：%s \n"%url + u"[*]存在Jboss漏洞" 
            models.zeroHistory(xTarget=url,xType='Java',xInfo='Ture').save()
        else:
            a = u"[*]目标：%s \n"%url + u"[*]未检测到反序列化漏洞" 
            models.zeroHistory(xTarget=url,xType='Java',xInfo='Fales').save()
        context['textValue'] = context1 + a
    elif modelss_ == "2":
       context2 = os.popen("pocsuite -r D:\\Python27\\Lib\\site-packages\\pocsuite\\tests\\dede_search.php_sqli.py -u %s"%url)
       x = context2.read().decode('utf-8')
       context['textValue'] = context1 + x
       models.zeroHistory(xTarget=url,xType='Python',xInfo='Fales').save()
    elif modelss_ == "0":
        context['testValue'] = '请选择模块......'
    else:
        pass
    # history.object.create(xTarget=url,xType='Java',xInfo='Ture')
    # models.zeroHistory(xTarget=url,xType='Java',xInfo='Ture').save()
    return render(request, 'index.html',context)
    
   
def poc_list(request):
    poc_list = []
    path = "..\Rescan\PocList"
    
    for root, dirs, files in os.walk('PocList'):  
        for file in files: 
            poc_dict = {'xtype':'','xname':'','xpath':''} 
            if os.path.splitext(file)[1] == '.py': 
                poc_dict['xtype'] = "Python"
                poc_dict['xname'] = os.path.splitext(file)[0] 
                poc_dict['xpath'] = path + '\\'+ os.path.join(file) 
            elif os.path.splitext(file)[1] == '.jar':
                poc_dict['xtype'] = "Java"
                poc_dict['xname'] = os.path.splitext(file)[0] 
                poc_dict['xpath'] = path + '\\'+ os.path.join(file)
            poc_list.append(poc_dict)

    return render(request,'poc_list.html',{'data':poc_list})

def xhistory(request):
    datax = models.zeroHistory.objects.all()
    return render(request,'history.html',{'data':datax})

def about(request):
    return render(request,'about.html')
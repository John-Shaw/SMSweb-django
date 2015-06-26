# coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from SMS.models import User
from django import forms


# 定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())

# class SearchForm(forms.Form):
#     studentID = forms.CharField(label='请输入学号：', max_length=100)

# 登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.get(username=username, password=password)
            if user:
                # HttpResponseRedirect('/search/')
                return render(request, 'search.html', {'username': username})
            else:
                # return render_to_response('success.html', {'username': username})
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf})

def search(request):
    if request.method == 'POST':
        studentid = request.POST['stdid']
        user = User.objects.get(studentID=studentid)
        if user:
            studentname = user.studentName
            return render_to_response('search.html', {'studentname': studentname,'username': studentid})
        else:
            # return render_to_response('search.html', {'studentname': 'test name'})
            return HttpResponseRedirect('/search')


    return render(request, 'search.html')
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html', {})

def user(request):
    return render(request,'blog/user.html',{})

def dataAnalyst(request):
    return render(request,'blog/dataAnalyst.html',{})

def admin(request):
    return render(request,'blog/admin.html',{})
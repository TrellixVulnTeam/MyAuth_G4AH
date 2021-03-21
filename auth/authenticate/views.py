from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as user_login

# Create your views here.


def index(request):
    return HttpResponse("He")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        user_login(request, user)
        # Redirect to a success page.
        return HttpResponse("成功")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("错误")

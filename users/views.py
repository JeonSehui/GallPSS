import json
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.http import JsonResponse
import json


class LoginView(View):
    def get(self, request):
        print("start")
        return render(request, "users/login.html")


def loginProc(request):
    if request.method == "POST":
        info = json.loads(request.body)
        user =authenticate(request, username=info['id'], password=info['password'])
        if user is not None:
            print("인증성공")
            login(request,user)
            print("로그인 성공")
            data = {'url': 'boards/main', 'login':True}
            return JsonResponse(data, status=200)
        else:
            print("인증실패")
            data = {'url': '', 'login':False}
            return JsonResponse(data=data, status=200)
    else:
        print("POST 아님")
        return render(request, 'users/login.html')


def log_out(request):
    logout(request)
    return redirect(reverse("core:loginMain"))

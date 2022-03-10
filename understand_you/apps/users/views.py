import json

from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.users.models import User

from utils.views import LoginRequiredJSONMixin


class LoginView(View):

    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        mobile = json_dict.get('mobile')
        password = json_dict.get('password')

        user = authenticate(username=mobile, password=password)

        login(request, user)

        request.session.set_expiry(None)

        res = JsonResponse({'code': 0, 'message': 'ok'})

        res.set_cookie('username', user.username, max_age=3600 * 24 * 15, samesite="None", secure=True)

        return res


class RegisterView(View):

    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        mobile = json_dict.get('mobile')
        sms = json_dict.get('sms')
        password = json_dict.get('password')

        if User.objects.filter(mobile=mobile):
            return JsonResponse({'message': '该手机号已注册！'})

        user = User.objects.create_user(mobile=mobile, password=password, username=mobile)

        login(request, user)

        return JsonResponse({'message': 'ok'})

class UserInfoViews(View):

    def get(self, request):

        login_user = request.user.username


        login_user_info = User.objects.filter(mobile=login_user)

        print(login_user_info.values("user_head")[0]["user_head"])

        user_info = {
            'mobile': login_user_info.values("mobile")[0]["mobile"],
            'user_head': login_user_info.values("user_head")[0]["user_head"],
            'user_name': login_user_info.values("user_name")[0]["user_name"],
            'password': login_user_info.values("password")[0]["password"],
            'gender': login_user_info.values("gender")[0]["gender"],
            'birthday': login_user_info.values("birthday")[0]["birthday"],
            'interest': login_user_info.values("interest")[0]["interest"],
            'personal_signature': login_user_info.values("personal_signature")[0]["personal_signature"],
            'address': login_user_info.values("address")[0]["address"],
            'user_fans_num': login_user_info.values("user_fans_num")[0]["user_fans_num"],
            'follow_num': login_user_info.values("follow_num")[0]["follow_num"],
            'user_collection': login_user_info.values("user_collection")[0]["user_collection"],
            'browsing_history': login_user_info.values("browsing_history")[0]["browsing_history"]
        }

        return JsonResponse({'code': 0, 'message': 'ok', 'data': user_info})
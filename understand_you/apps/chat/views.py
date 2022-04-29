from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.users.models import User, UserFollow

class ContactsViews(View):

    def get(self, request):
        # 获取当前登录用户的id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 存储用户关注人的列表
        user_follow_list = []
        # 获取用户关注的人
        user_follow = UserFollow.objects.filter(Q(user_id=user_id)&Q(is_follow=1))
        # 将被关注人的基础信息提取出来
        for user in user_follow:
            contacts = User.objects.filter(user_id=user.follow_user_id)

            if contacts.values("user_head")[0]["user_head"][0] == "{":
                user_head = contacts.values("user_head")[0]["user_head"][54:-2]
            else:
                user_head = contacts.values("user_head")[0]["user_head"]

            user_follow_list.append({
                "user_id": contacts.values("user_id")[0]["user_id"],
                "user_head": user_head,
                "user_name": contacts.values("user_name")[0]["user_name"]
            })

        return JsonResponse({'code': 0, 'message': 'ok', "data": user_follow_list})
import json

from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.users.models import User, UserCollection, UserLike, UserFollow

from apps.articles.models import Article


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
        if login_user == "":
            return JsonResponse({'code': 0, 'message': 'ok'})

        login_user_info = User.objects.filter(mobile=login_user)

        interest = str(login_user_info.values("interest")[0]["interest"]).replace('[', '').replace(']', '').replace("'", "").replace(" ", "").split(',')

        if login_user_info.values("user_head")[0]["user_head"][0] == "{":
            user_head = login_user_info.values("user_head")[0]["user_head"][54:-2]
        else:
            user_head = login_user_info.values("user_head")[0]["user_head"]

        user_info = {
            'user_id': login_user_info.values("user_id")[0]["user_id"],
            'mobile': login_user_info.values("mobile")[0]["mobile"],
            'user_head': user_head,
            'user_name': login_user_info.values("user_name")[0]["user_name"],
            'password': login_user_info.values("password")[0]["password"],
            'gender': login_user_info.values("gender")[0]["gender"],
            'birthday': login_user_info.values("birthday")[0]["birthday"],
            'interest': interest,
            'personal_signature': login_user_info.values("personal_signature")[0]["personal_signature"],
            'address': login_user_info.values("address")[0]["address"],
            'user_fans_num': login_user_info.values("user_fans_num")[0]["user_fans_num"],
            'follow_num': login_user_info.values("follow_num")[0]["follow_num"],
            'user_collection': login_user_info.values("user_collection")[0]["user_collection"],
            'browsing_history': login_user_info.values("browsing_history")[0]["browsing_history"]
        }

        return JsonResponse({'code': 0, 'message': 'ok', 'data': user_info})

class ChangeUserInfoViews(View):

    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        user_head = json_dict.get("user_head")
        user_name = json_dict.get("user_name")
        gender = json_dict.get("gender")
        birthday = json_dict.get("birthday")
        interest = json_dict.get("interest")
        personal_signature = json_dict.get("personal_signature")
        address = json_dict.get("address")

        interest_list = []
        # interest = interest.remove('')
        for value in interest:
            if value != '':
                interest_list.append(value)
            print(interest_list)

        login_user = request.user.username

        user_info = User.objects.get(mobile=login_user)
        user_info.user_head = user_head
        user_info.user_name = user_name
        user_info.gender = gender
        user_info.birthday = birthday
        user_info.interest = interest_list
        user_info.personal_signature = personal_signature
        user_info.address = address

        user_info.save()

        return JsonResponse({'code': 0, 'message': 'ok'})

class LogoutView(View):

    def delete(self, request):
        """实现退出登录逻辑"""
        # 清理session
        logout(request)

        # 退出登录，重定向到登录页
        response = JsonResponse({'code': 0,
                                 'message': 'ok'})
        # 退出登录时清除cookie中的username
        response.delete_cookie('username')

        return response

# 用户收藏
class UserCollectionViews(View):

    def post(self, request):

        # 获取前端传来的文章id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_id = json.loads(json_str)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置文章收藏状态
        is_collection = True
        # 判断该收藏字段是否存在，存在则更改，不存在则创建
        user_collertions = UserCollection.objects.filter(user_id=user_id, article_id=article_id)
        if user_collertions:
            user_collertions.update(
                is_collection=is_collection,
            )
        else:
            UserCollection.objects.create(
                user_id=user_id,
                is_collection=is_collection,
                article_id=article_id
            )
        # 计算用户收藏数
        collection_nums = 0
        collection_list = UserCollection.objects.filter(user_id=user_id, is_collection=True)
        for value in collection_list:
            collection_nums += 1
        # 更改用户收藏数
        user_info.update(
            user_collection=collection_nums
        )
        # 计算文章被收藏数
        article_collection_nums = 0
        article_collection_list = UserCollection.objects.filter(article_id=article_id, is_collection=True).values()
        for value in article_collection_list:
            article_collection_nums += 1
        # 更改文章总收藏数
        article_collection = Article.objects.filter(article_id=article_id)
        article_collection.update(
            article_collection=article_collection_nums
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })

# 取消收藏
class CancelCollectionViews(View):

    def post(self, request):

        # 获取前端传来的文章id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_id = json.loads(json_str)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置文章收藏状态
        is_collection = False
        # 获取需要更改的字段并进行更改
        user_collertions = UserCollection.objects.filter(user_id=user_id, article_id=article_id)
        user_collertions.update(
            is_collection=is_collection
        )
        # 计算用户收藏数
        collection_nums = 0
        collection_list = UserCollection.objects.filter(user_id=user_id, is_collection=True)
        for value in collection_list:
            collection_nums += 1
        # 更改用户收藏数
        user_info.update(
            user_collection=collection_nums
        )
        # 计算文章被收藏数
        article_collection_nums = 0
        article_collection_list = UserCollection.objects.filter(article_id=article_id, is_collection=True).values()
        for value in article_collection_list:
            article_collection_nums += 1
        # 更改文章总收藏数
        article_collection = Article.objects.filter(article_id=article_id)
        article_collection.update(
            article_collection=article_collection_nums
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })

# 用户点赞
class UserLikeViews(View):

    def post(self, request):

        # 获取前端传来的文章id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_id = json.loads(json_str)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置文章点赞状态
        is_like = True
        # 判断该点赞字段是否存在，存在则更改，不存在则创建
        user_like = UserLike.objects.filter(user_id=user_id, article_id=article_id)
        if user_like:
            user_like.update(
                is_like=is_like,
            )
        else:
            UserLike.objects.create(
                user_id=user_id,
                is_like=is_like,
                article_id=article_id
            )
        # 计算文章被点赞数
        article_like_nums = 0
        article_like_list = UserLike.objects.filter(article_id=article_id, is_like=True).values()
        for value in article_like_list:
            article_like_nums += 1
        # 更改文章总收藏数
        article_like = Article.objects.filter(article_id=article_id)
        article_like.update(
            article_like=article_like_nums
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })

# 取消点赞
class CancelLikeViews(View):

    def post(self, request):

        # 获取前端传来的文章id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_id = json.loads(json_str)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置文章点赞状态
        is_like = False
        # 获取该字段更改状态
        user_like = UserLike.objects.filter(user_id=user_id, article_id=article_id)
        user_like.update(
            is_like=is_like,
        )
        # 计算文章被点赞数
        article_like_nums = 0
        article_like_list = UserLike.objects.filter(article_id=article_id, is_like=True).values()
        for value in article_like_list:
            article_like_nums += 1
        # 更改文章总收藏数
        article_like = Article.objects.filter(article_id=article_id)
        article_like.update(
            article_like=article_like_nums
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })

class UserFollowViews(View):

    def post(self, request):

        # 获取前端传来的文章作者id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_user_id = json.loads(json_str)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置用户关注状态
        is_follow = True
        # 判断该关注字段是否存在，存在则更改，不存在则创建
        user_follow = UserFollow.objects.filter(user_id=user_id, follow_user_id=article_user_id)
        if user_follow:
            user_follow.update(
                is_follow=is_follow,
            )
        else:
            UserFollow.objects.create(
                user_id=user_id,
                is_follow=is_follow,
                follow_user_id=article_user_id
            )

        # 计算用户关注数
        follow_num = 0
        follow_list = UserFollow.objects.filter(user_id=user_id, is_follow=True)
        for value in follow_list:
            follow_num += 1
        # 更改用户关注数
        user_info.update(
            follow_num=follow_num
        )

        # 计算被关注用户粉丝数
        user_fans_num = 0
        fans_list = UserFollow.objects.filter(follow_user_id=article_user_id, is_follow=True)
        for value in fans_list:
            user_fans_num += 1
        # 更改被关注用户粉丝数
        User.objects.filter(user_id=article_user_id).update(
            user_fans_num=user_fans_num
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })

class CancelFollowViews(View):

    def post(self, request):

        # 获取前端传来的文章作者id
        json_bytes = request.body
        json_str = json_bytes.decode()
        article_user_id = json.loads(json_str)
        print("文章作者id ->", article_user_id)
        # 获取当前登录用户id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 设置用户关注状态
        is_follow = False
        # 更改状态
        user_follow = UserFollow.objects.filter(user_id=user_id, follow_user_id=article_user_id)
        user_follow.update(
            is_follow=is_follow,
        )

        # 计算用户关注数
        follow_num = 0
        follow_list = UserFollow.objects.filter(user_id=user_id, is_follow=True)
        for value in follow_list:
            follow_num += 1
        # 更改用户关注数
        user_info.update(
            follow_num=follow_num
        )

        # 计算被关注用户粉丝数
        user_fans_num = 0
        fans_list = UserFollow.objects.filter(follow_user_id=article_user_id, is_follow=True)
        for value in fans_list:
            user_fans_num += 1
        # 更改被关注用户粉丝数
        User.objects.filter(user_id=article_user_id).update(
            user_fans_num=user_fans_num
        )

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })


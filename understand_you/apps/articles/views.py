import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import View

from apps.users.models import User, UserLike, UserCollection, UserFollow

from apps.articles.models import Article


class ReleaseArticleViews(View):

    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        login_user = request.user.username

        article_title = json_dict.get("article_title")
        article_belong = json_dict.get("article_belong")
        article_label = json_dict.get("article_label")
        article_img = json_dict.get("article_img")
        article_content = json_dict.get("content")
        article_uptime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        user_id = User.objects.filter(mobile=login_user).values("user_id")[0]["user_id"]

        article = Article.objects.create(article_title=article_title,
                                         article_belong=article_belong,
                                         article_label=article_label,
                                         article_img=article_img[0]['content'],
                                         article_content=article_content,
                                         article_uptime=article_uptime,
                                         user_id=user_id)

        return JsonResponse({'code': 0, 'message': 'ok'})

class ArticleViews(View):

    def get(self, request):

        articleList = Article.objects.all()

        articleInfoList = []
        # 查找当前登录用户的user_id
        login_user = request.user.username
        user_info = User.objects.filter(username=login_user)
        user_id = user_info.values("user_id")[0]["user_id"]
        # 倒序输出,使最新发布的文章在前面
        for value in articleList[::-1]:

            articleUserInfo = User.objects.filter(user_id=value.user_id)
            # 判断头像类型,并根据类型进行修改
            if articleUserInfo.values("user_head")[0]["user_head"][0] == "{":
                user_head = articleUserInfo.values("user_head")[0]["user_head"][54:-2]
            else:
                user_head = articleUserInfo.values("user_head")[0]["user_head"]

            # 登录用户对文章的收藏状态
            if UserCollection.objects.filter(user_id=user_id, article_id=value.article_id):
                user_collection_article = UserCollection.objects.filter(user_id=user_id, article_id=value.article_id).values("is_collection")[0]["is_collection"]
            else:
                user_collection_article = False

            # 登录用户对文章的点赞状态
            if UserLike.objects.filter(user_id=user_id, article_id=value.article_id):
                user_like_article = UserLike.objects.filter(user_id=user_id, article_id=value.article_id).values("is_like")[0]["is_like"]
            else:
                user_like_article = False

            # 登录用户对文章的点赞状态
            if UserFollow.objects.filter(user_id=user_id, follow_user_id=value.user_id):
                user_follow = UserFollow.objects.filter(user_id=user_id, follow_user_id=value.user_id).values("is_follow")[0]["is_follow"]
            else:
                user_follow = False


            # 将获取到的用户信息存入对象中
            articleInfo = {
                'user_name': articleUserInfo.values("user_name")[0]["user_name"],
                'user_head': user_head,
                'article_id': value.article_id,
                'article_title': value.article_title,
                'article_belong': value.article_belong,
                'article_label': value.article_label,
                'article_img': value.article_img,
                'article_content': value.article_content,
                'article_uptime': value.article_uptime,
                'user_id': value.user_id,
                'user_follow': user_follow,
                'article_views': value.article_views,
                'article_like': value.article_like,
                'user_collection_article': user_collection_article,
                'user_like_article': user_like_article,
                'article_collection': value.article_collection,
                'article_forward': value.article_forward,
                'article_comments_num': value.article_comments_num,
            }
            articleInfoList.append(articleInfo)

        return JsonResponse({'code': 0, 'message': 'ok', 'data': articleInfoList})


class SearchViews(View):

    def post(self, request):

        # 获取搜索的关键词
        json_bytes = request.body
        search_keyword = json_bytes.decode()
        # 获取文章标题包含搜索关键词的字段
        article_title = Article.objects.filter(article_title__icontains=search_keyword)
        # 用于存储包含字段的列表
        article_list = []
        for i in range(len(article_title)):
            print(article_title.values("article_title")[i]["article_title"])

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })
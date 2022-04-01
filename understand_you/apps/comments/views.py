import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import View


class WriteCommentViews(View):

    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)

        comment_content = json_dict.get('comment_content')
        comment_type = json_dict.get('comment_type')
        comment_uptime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        article_id = json_dict.get('article_index')

        print(comment_content)
        print('当前时间-->', comment_uptime)
        print(article_id)

        return JsonResponse({
            'code': 0,
            'message': 'ok'
        })
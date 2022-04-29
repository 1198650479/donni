from django.urls import re_path
from apps.chat import consumers

websocket_urlpatterns = [
    re_path(r'chat/(?P<chat_id>\w+)/(?P<user_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
# from channels.auth import AuthMiddlewareStack
from . import routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'understand_you.settings')

application = ProtocolTypeRouter({
     # 告诉 Channels 当 Channels 服务器接收到 HTTP 请求时要运行什么代码
     "http": get_asgi_application(),
     "websocket": URLRouter(
            routings.websocket_urlpatterns
        )
})

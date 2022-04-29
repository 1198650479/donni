from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    id_max = 0
    id_min = 0
    # 有客户端来向后端发送websocket连接的请求时,自动触发
    def websocket_connect(self, message):
        global id_max, id_min, user_id
        # 服务端接受和客户端创建连接
        print("连接成功")
        self.accept()
        chat_id = self.scope["url_route"]["kwargs"].get("chat_id")
        user_id = self.scope["url_route"]["kwargs"].get("user_id")

        if chat_id > user_id:
            id_max = chat_id
            id_min = user_id
        else:
            id_max = user_id
            id_min = chat_id

        print("被访问者ID:" + chat_id, "访问者ID:" + user_id)
        print(id_min + id_max)

        async_to_sync(self.channel_layer.group_add)(id_min + id_max, self.channel_name)

    # 浏览器基于websocket向后端发送数据，自动触发接收消息
    def websocket_receive(self, message):
        # 给浏览器回复消息
        async_to_sync(self.channel_layer.group_send)(id_min + id_max, {"type": "chat_send", "message": message})

    def chat_send(self, event):
        user_id = self.scope["url_route"]["kwargs"].get("user_id")
        text = event['message']['text']
        print(user_id + "--->" + text)
        # self.send({
        #     "id": user_id,
        #     "content": text
        # })
        self.send(user_id + ":" + text)

    # 客户端与服务端断开连接时，自动触发
    def websocket_disconnect(self, message):
        async_to_sync(self.channel_layer.group_discard)(id_min + id_max, self.channel_name)
        raise StopConsumer()

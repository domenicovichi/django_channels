from django.urls import re_path

import chat.consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', chat.consumer.ChatConsumer.as_asgi()),
]
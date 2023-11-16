# chat/urls.py
from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', consumers.ChatConsumer.as_asgi()),
]

app_name = 'chat'

router_chatroom = DefaultRouter()
router_chatroom.register(r'chatroom', ModelViewSetChatRoom)

router_message = DefaultRouter()
router_message.register(r'Messages', ModelViewSetMessage)

urlpatterns = [
    path('room/<int:room_id>/', chat_room, name='chat_room'),
    path('chatroom/', include(router_chatroom.urls)),
    path('messsage/', include(router_message.urls)),
]

# Include the WebSocket URL patterns
urlpatterns += websocket_urlpatterns

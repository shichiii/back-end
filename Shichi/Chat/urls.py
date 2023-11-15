# chat/urls.py
from django.urls import path
from .views import *

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', consumers.ChatConsumer.as_asgi()),
]

app_name = 'chat'

urlpatterns = [
    path('room/<int:room_id>/', chat_room, name='chat_room'),
]

# Include the WebSocket URL patterns
urlpatterns += websocket_urlpatterns

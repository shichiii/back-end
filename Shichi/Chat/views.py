from django.shortcuts import render
from rest_framework import viewsets
from .models import ChatRoom , Message
from CustomAdvertisement.models import CustomAdvertisement
from .serializers import ChatRoomSerializers , MessageSerializers
from rest_framework.response import Response
from rest_framework import status


def chat_room(request, room_id):
    return render(request, 'chat/chat.html')

class ModelViewSetChatRoom(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializers

class ModelViewSetMessage(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
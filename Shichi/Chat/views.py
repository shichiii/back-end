from django.shortcuts import render
from rest_framework import viewsets , views
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

class ModelViewSetMessage(views.APIView):
    serializer_class = MessageSerializers
    queryset = Message.objects.all()

    def get(self, request, room_id):
        try:
            queryset = Message.objects.filter(room=room_id)
        except Message.DoesNotExist:
            return Response("not found", status=status.HTTP_404_NOT_FOUND)

        serializer = MessageSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework import viewsets , views
from .models import ChatRoom , Message
from CustomUser.models import CustomUser
from CustomAdvertisement.models import CustomAdvertisement
from .serializers import ChatRoomSerializers , MessageSerializers , ChatRoomSerializersget
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes


def chat_room(request, room_id):
    return render(request, 'chat/chat.html') 

class ModelViewSetChatRoom(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializersget

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

class PersonChatRoomsAPIView(views.APIView):
    def get(self, request):
        try:
            if request.user.is_anonymous:
                return Response({"error": "Authorization needed"}, status=status.HTTP_401_UNAUTHORIZED)
            chat_rooms = ChatRoom.objects.filter(sender=request.user.id) | ChatRoom.objects.filter(reciver=request.user.id)
            serializer = ChatRoomSerializersget(chat_rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def DoesHaveRome2Person(request, sender_id, reciver_id):
    try:
        chat_room = ChatRoom.objects.get(sender=sender_id, reciver=reciver_id)
        return Response(chat_room.id, status=status.HTTP_200_OK)
    except ChatRoom.DoesNotExist:
        return Response(False, status=status.HTTP_200_OK)
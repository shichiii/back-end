from rest_framework import serializers
from .models import ChatRoom , Message

class ChatRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
from rest_framework import serializers
from .models import ChatRoom , Message
from CustomUser.models import CustomUser

class CustomUserInRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id' , 'first_name' , 'last_name' , 'profile_image' ]  # Include the fields you want in the response
class ChatRoomSerializers(serializers.ModelSerializer):
    sender = CustomUserInRoomSerializer()
    reciver = CustomUserInRoomSerializer()
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'



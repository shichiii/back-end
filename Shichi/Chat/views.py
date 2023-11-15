from django.shortcuts import render

def chat_room(request, room_id):
    return render(request, 'chat/chat.html')
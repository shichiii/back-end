import json
from channels.auth import AuthMiddlewareStack , login
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from .models import ChatRoom, Message
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from CustomUser.models import CustomUser
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken

class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Get the query string from the scope
        query_string = scope.get("query_string", b"").decode("utf-8")

        # Parse the query string to get the token
        token_param = next((param.split("=") for param in query_string.split("&") if param.startswith("token=")), None)

        if token_param:
            # Get the user from the token and set it in the scope
            user = await self.get_user_from_token(token_param[1])
            scope["user"] = user

        return await super().__call__(scope, receive, send)
    @database_sync_to_async
    def get_user_from_token(self, access_token):
        try:
            decoded_token = AccessToken(token=access_token)
            user = CustomUser.objects.get(id=decoded_token['user_id'])
            return user
        except Exception as e:
        # Handle token decoding errors
            print(f"Error decoding token: {e}")
        return AnonymousUser()  # Replace with your logic
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        # await login(self.scope, user)
        # breakpoint() 
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # breakpoint()
        sender = self.scope['user'].last_name
        user = self.scope['user']
        # print(f"User {user} sent a message: {text_data}")
        if sender == "" :
            sender = "Anonymous"
        message = json.loads(text_data)
        message = message["message"]
        message_send = {}
        message_send['message'] = message
        message_send['sender'] = sender
        # Register the message in the database.
        chat_room = sync_to_async( ChatRoom.objects.get)(id=self.room_id)
        message_save = sync_to_async( Message.objects.create)(room=chat_room, sender=self.scope['user'], content=message)

        # Broadcast message to a room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': json.dumps(message_send),
            }
        )

    async def send_message(self, event):
        # Send a message to WebSocket
        await self.send(text_data=event['message'])

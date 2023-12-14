from django.db import models
from CustomUser.models import CustomUser

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='sent_messages')
    reciver = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='received_messages')

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
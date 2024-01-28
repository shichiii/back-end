from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from rest_framework import permissions, status

from Chat.models import ChatRoom


class IsRoomMember(BasePermission):
    def has_permission(self, request, view):
        return ChatRoom.objects.filter(user=request.user, room_id=view.kwargs['pk']).exists()
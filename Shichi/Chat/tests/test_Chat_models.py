import pytest
from django.urls import reverse
from rest_framework import status
from model_bakery import baker
from rest_framework.test import APIClient
from Chat.models import ChatRoom, Message, CustomUser

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return baker.make(CustomUser)

@pytest.fixture
def chat_room(user):
    return baker.make(ChatRoom, sender=user, reciver=user)

@pytest.fixture
def message(chat_room, user):
    return baker.make(Message, room=chat_room, sender=user)

@pytest.mark.django_db
def test_chat_room_model():
    user = baker.make(CustomUser)
    chat_room = baker.make(ChatRoom, sender=user, reciver=user, name="Test Room")

    assert str(chat_room) == "Test Room"
    assert chat_room.sender == user
    assert chat_room.reciver == user

@pytest.mark.django_db
def test_message_model():
    user = baker.make(CustomUser)
    chat_room = baker.make(ChatRoom, sender=user, reciver=user)
    message = baker.make(Message, room=chat_room, sender=user, content="Hello!")

    assert str(message) == "Hello!"
    assert message.room == chat_room
    assert message.sender == user
    assert message.content == "Hello!"

@pytest.mark.django_db
def test_chat_room_creation(api_client, user):
    api_client.force_authenticate(user=user)

    url = 'http://localhost:8000/chat/chatroom/chatroom/' 
    response = api_client.post(url, {'name': 'New Room', 'reciver': user.id , 'sender': user.id})

    assert response.status_code == status.HTTP_201_CREATED
    assert ChatRoom.objects.count() == 1
    assert response.data['name'] == 'New Room'
    assert response.data['sender'] == user.id
    assert response.data['reciver'] == user.id


@pytest.mark.django_db
def test_get_messages(api_client, user, chat_room, message):
    api_client.force_authenticate(user=user)

    url = reverse('chat:message-list', kwargs={'room_id': chat_room.id})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['content'] == message.content

@pytest.mark.django_db
def test_get_person_chat_rooms(api_client, user, chat_room):
    api_client.force_authenticate(user=user)

    url = reverse('chat:my_rooms')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == chat_room.name

@pytest.mark.django_db
def test_create_chat_room_invalid_user(api_client, user):
    api_client.force_authenticate(user=user)

    url = 'http://localhost:8000/chat/chatroom/chatroom/' 
    response = api_client.post(url, {'name': 'New Room', 'reciver': 9999 , 'sender': user.id})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert ChatRoom.objects.count() == 0

@pytest.mark.django_db
def test_get_messages_invalid_room(api_client, user):
    api_client.force_authenticate(user=user)

    invalid_room_id = 9923499  # Assuming this room ID does not exist
    url = reverse('chat:message-list', kwargs={'room_id': invalid_room_id})
    response = api_client.get(url)
    print(response.data)

    assert response.data == []

@pytest.mark.django_db
def test_get_person_chat_rooms_empty(api_client, user):
    api_client.force_authenticate(user=user)

    url = reverse('chat:my_rooms')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0

@pytest.mark.django_db
def test_get_messages_empty(api_client, user, chat_room):
    api_client.force_login(user)

    url = reverse('chat:message-list', kwargs={'room_id': chat_room.id})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_person_chat_rooms_anonymous_user(api_client):
    url = reverse('chat:my_rooms')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
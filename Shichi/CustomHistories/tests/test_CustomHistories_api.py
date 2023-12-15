import pytest 
from django.urls import reverse 
from rest_framework import status 
from rest_framework.test import APIClient 
from .models import CustomHistories, CustomAdvertisement 
from .serializers import CustomHistoriesSerializer 
 
 
@pytest.fixture 
def api_client(): 
    return APIClient() 
 
 
@pytest.fixture 
def user(): 
    from django.contrib.auth.models import User 
    return User.objects.create_user(username='testuser', password='testpass') 
 
 
@pytest.mark.django_db 
def test_custom_histories_list(api_client, user): 
    ad = CustomAdvertisement.objects.create(title="Test Ad", description="Test Description", owner=user) 
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take") 
 
    api_client.force_login(user) 
    url = reverse('CustomHistories_list') 
    response = api_client.get(url) 
 
    assert response.status_code == status.HTTP_202_ACCEPTED 
    assert len(response.data) == 1 
    assert response.data[0]['advertisement']['title'] == ad.title 
    assert response.data[0]['take_or_own'] == history.take_or_own 

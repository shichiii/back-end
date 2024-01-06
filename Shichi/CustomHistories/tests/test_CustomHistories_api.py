import pytest 
from django.urls import reverse 
from django.utils import timezone 
from rest_framework import status 
from model_bakery import baker
from rest_framework.test import APIClient 
from CustomHistories.models import CustomHistories, CustomAdvertisement 
from CustomHistories.serializers import CustomHistoriesSerializer 
from CustomAdvertisement.models import CustomAdvertisement
from CustomUser.models import CustomUser
 
 
@pytest.fixture 
def api_client(): 
    return APIClient() 
 
 
@pytest.fixture 
def user(): 
    return baker.make(CustomUser)  

@pytest.fixture
def custom_advertisement():
    return baker.make(CustomAdvertisement)

@pytest.fixture
def custom_history(user, custom_advertisement):
    return baker.make(CustomHistories, advertisement=custom_advertisement, take_or_own="take", user=user)
 
 
@pytest.mark.django_db 
def test_custom_histories_list(api_client , user):  
    user = baker.make(CustomUser)
    api_client.force_authenticate(user=user)
    ad = baker.make(CustomAdvertisement)  
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take" , user = user) 
 
    url = reverse('CustomHistories_list') 
    response = api_client.get(url)
    print(response.data) 
 
    assert response.status_code == status.HTTP_202_ACCEPTED 
    assert len(response.data) == 1 
    assert response.data[0]['created_date'] is not None
    assert CustomHistories.objects.count() == 1
    assert CustomAdvertisement.objects.count() == 1
    assert response.data[0]['take_or_own'] == history.take_or_own 
    assert history.created_date <= timezone.now() 

@pytest.mark.django_db 
def test_custom_histories_404(api_client): 
    
    user = baker.make(CustomUser)
    print(user)  
    api_client.force_login(user) 
    url = reverse('CustomHistories_list') 
    response = api_client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert len(response.data) == 0

@pytest.mark.django_db 
def test_custom_histories_viewset_list(api_client, user, custom_history):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-list')  # Adjust the endpoint name based on your project

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['take_or_own'] == custom_history.take_or_own

@pytest.mark.django_db 
def test_custom_histories_viewset_create(api_client, user, custom_advertisement):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-list')  # Adjust the endpoint name based on your project

    data = {
        'advertisement': custom_advertisement.id,
        'take_or_own': 'take',
        'user' : user.id
    }

    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert CustomHistories.objects.count() == 1
    assert CustomHistories.objects.first().take_or_own == 'take'

@pytest.mark.django_db 
def test_custom_histories_viewset_retrieve(api_client, user, custom_history):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-detail', args=[custom_history.id])  # Adjust the endpoint name based on your project

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['take_or_own'] == custom_history.take_or_own

@pytest.mark.django_db 
def test_custom_histories_viewset_update(api_client, user, custom_history):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-detail', args=[custom_history.id])

    data = {
        'take_or_own': 'own',
        'advertisement': custom_history.advertisement.id,  # Include the advertisement ID
        'id': custom_history.id , 
        'user' : user.id
    }

    response = api_client.put(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert CustomHistories.objects.first().take_or_own == 'own'


@pytest.mark.django_db 
def test_custom_histories_viewset_delete(api_client, user, custom_history):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-detail', args=[custom_history.id])  # Adjust the endpoint name based on your project

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert CustomHistories.objects.count() == 0

@pytest.mark.django_db
def test_custom_histories_viewset_list_multiple(api_client, user):
    api_client.force_login(user)
    custom_history_1 = baker.make(CustomHistories, user=user)
    custom_history_2 = baker.make(CustomHistories, user=user)

    url = reverse('customhistoriesbackdoor-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['take_or_own'] == custom_history_1.take_or_own
    assert response.data[1]['take_or_own'] == custom_history_2.take_or_own

@pytest.mark.django_db
def test_custom_histories_viewset_delete_not_found(api_client, user):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-detail', args=[999])  # Non-existent ID

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert CustomHistories.objects.count() == 0

@pytest.mark.django_db
def test_custom_histories_viewset_retrieve_not_found(api_client, user):
    api_client.force_login(user)
    url = reverse('customhistoriesbackdoor-detail', args=[999])  # Non-existent ID

    response = api_client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND

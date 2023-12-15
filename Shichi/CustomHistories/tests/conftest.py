# from django.urls import reverse
# from rest_framework.test import APIClient
# import pytest

# @pytest.fixture
# def api_client():
#     return APIClient()

# @pytest.fixture
# def CustomHistories_list_view_url():
#     return reverse('CustomHistories_list')


import pytest 
from django.utils import timezone 
from .models import CustomHistories, CustomAdvertisement 
 
 
@pytest.mark.django_db 
def test_create_custom_history(): 
    ad = CustomAdvertisement.objects.create(title="Test Ad", description="Test Description") 
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take") 
    assert history.created_date <= timezone.now() 
 
 
@pytest.mark.django_db 
def test_custom_history_str(): 
    ad = CustomAdvertisement.objects.create(title="Test Ad", description="Test Description") 
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take") 
    assert str(history) == f"history.advertisement.title - history.take_or_own" 
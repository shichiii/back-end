import pytest 
from django.utils import timezone 
from model_bakery import baker
from CustomUser.models import CustomUser
from CustomHistories.models import CustomHistories, CustomAdvertisement 


@pytest.mark.django_db 
def test_create_custom_history(): 
    ad = baker.make(CustomUser)
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take" ) 
    assert history.created_date <= timezone.now() 


@pytest.mark.django_db 
def test_custom_history_str(): 
    ad = CustomAdvertisement.objects.create(title="Test Ad", description="Test Description") 
    history = CustomHistories.objects.create(advertisement=ad, take_or_own="take") 
    assert str(history) == f"history.advertisement.title - history.take_or_own" 
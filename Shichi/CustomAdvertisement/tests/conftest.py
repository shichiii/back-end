from django.urls import reverse
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def advertisement_list_view_url():
    return reverse('advertisement_list')

@pytest.fixture
def advertisement_detail_view_url():
    def do_advertisement_detail_view_url(advertisement_id):
        return reverse('advertisement_show', kwargs={'id': advertisement_id})

    return do_advertisement_detail_view_url

@pytest.fixture
def advertisement_create_view_url():
    return reverse('advertisement_create')

@pytest.fixture
def advertisement_delete_view_url():
    def do_advertisement_delete_view_url(advertisement_id):
        return reverse('advertisement_delete', kwargs={'pk': advertisement_id})
    
    return do_advertisement_delete_view_url

@pytest.fixture
def advertisement_update_view_url():
    def do_advertisement_update_view_url(advertisement_id):
        return reverse('advertisement_update', kwargs={'pk': advertisement_id})
    
    return do_advertisement_update_view_url
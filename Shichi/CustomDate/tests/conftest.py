from django.urls import reverse
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def date_list_view_url():
    return reverse('date-list')

@pytest.fixture
def date_detail_view_url():
    def do_date_detail_view_url(date_id):
        return reverse('date-show', kwargs={'id': date_id})

    return do_date_detail_view_url

@pytest.fixture
def date_create_view_url():
    return reverse('date-create')

@pytest.fixture
def date_delete_view_url():
    def do_date_delete_view_url(date_id):
        return reverse('date-delete', kwargs={'pk': date_id})
    
    return do_date_delete_view_url

@pytest.fixture
def date_update_view_url():
    def do_date_update_view_url(date_id):
        return reverse('date-update', kwargs={'pk': date_id})
    
    return do_date_update_view_url
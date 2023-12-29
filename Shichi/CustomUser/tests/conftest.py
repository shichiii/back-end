from django.urls import reverse
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_list_view_url():
    return reverse('list')

@pytest.fixture
def user_detail_view_url():
    def do_user_detail_view_url(user_id):
        return reverse('myshow', kwargs={'id': user_id})

    return do_user_detail_view_url

@pytest.fixture
def user_create_view_url():
    return reverse('create')

@pytest.fixture
def user_delete_view_url():
    def do_user_delete_view_url(user_id):
        return reverse('delete', kwargs={'pk': user_id})
    
    return do_user_delete_view_url

@pytest.fixture
def user_update_view_url():
    def do_user_update_view_url(user_id):
        return reverse('update', kwargs={'pk': user_id})
    
    return do_user_update_view_url

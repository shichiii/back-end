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
    return reverse('advertisement_show')

@pytest.fixture
def advertisement_create_view_url():
    return reverse('advertisement_create')
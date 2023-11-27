import pytest
from rest_framework import status
from model_bakery import baker
from CustomAdvertisement.models import CustomAdvertisement

@pytest.mark.django_db
class TestCustomAdvertisementViewSet:
    
    def test_if_get_request_is_status_200(self, api_client, advertisement_list_view_url):
        response = api_client.get(advertisement_list_view_url)
        assert response.status_code == status.HTTP_200_OK

    def test_if_post_request_is_status_405(self, api_client, advertisement_list_view_url):
        response = api_client.post(advertisement_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_list_view_url):
        response = api_client.put(advertisement_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_list_view_url):
        response = api_client.patch(advertisement_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_list_view_url):
        response = api_client.delete(advertisement_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
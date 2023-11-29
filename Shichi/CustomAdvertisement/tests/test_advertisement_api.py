import pytest
from rest_framework import status
from model_bakery import baker
from CustomAdvertisement.models import CustomAdvertisement

@pytest.mark.django_db
class TestCustomAdvertisementViewSet:

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
        
    def test_get_request_returns_objects(self, api_client, advertisement_list_view_url):
        baker.make(CustomAdvertisement, _quantity=3)
        
        response = api_client.get(advertisement_list_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3 
        
@pytest.mark.django_db
class TestCustomAdvertisementShowView:

    def test_if_post_request_is_status_405(self, api_client, advertisement_detail_view_url):
        response = api_client.post(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_detail_view_url):
        response = api_client.put(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_detail_view_url):
        response = api_client.patch(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_detail_view_url):
        response = api_client.delete(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_get_request_returns_object(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)

        response = api_client.get(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == obj.id  

    def test_get_request_nonexistent_object_returns_404(self, api_client, advertisement_detail_view_url):
        response = api_client.get(advertisement_detail_view_url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
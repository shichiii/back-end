import pytest
from rest_framework import status
from model_bakery import baker
from CustomAdvertisement.models import CustomAdvertisement

@pytest.mark.django_db
class TestCustomAdvertisementSearchView:
    def test_if_post_request_is_status_405(self, api_client, advertisement_search_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.post(advertisement_search_view_url(obj.car_name))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_search_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.put(advertisement_search_view_url(obj.car_name))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_search_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.patch(advertisement_search_view_url(obj.car_name))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_search_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.delete(advertisement_search_view_url(obj.car_name))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_if_get_request_returns_objects(self, api_client, advertisement_search_view_url):
        obj = baker.make(CustomAdvertisement)

        response = api_client.get(advertisement_search_view_url(obj.car_name))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_nonexistent_object(self, api_client, advertisement_search_view_url):
        response = api_client.get(advertisement_search_view_url('x'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
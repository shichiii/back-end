import pytest
from rest_framework import status
from model_bakery import baker
from CustomDate.models import CustomDate
from CustomAdvertisement.models import CustomAdvertisement
from datetime import datetime

@pytest.mark.django_db
class TestCustomDateViewSet:

    def test_if_post_request_is_status_405(self, api_client, date_list_view_url):
        response = api_client.post(date_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, date_list_view_url):
        response = api_client.put(date_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, date_list_view_url):
        response = api_client.patch(date_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, date_list_view_url):
        response = api_client.delete(date_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_if_get_request_returns_objects(self, api_client, date_list_view_url):
        baker.make(CustomDate, _quantity=3)
        
        response = api_client.get(date_list_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3 
        
@pytest.mark.django_db
class TestCustomDateShowView:

    def test_if_post_request_is_status_405(self, api_client, date_detail_view_url):
        obj = baker.make(CustomDate)
        
        response = api_client.post(date_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, date_detail_view_url):
        obj = baker.make(CustomDate)
        
        response = api_client.put(date_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, date_detail_view_url):
        obj = baker.make(CustomDate)
        
        response = api_client.patch(date_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, date_detail_view_url):
        obj = baker.make(CustomDate)
        
        response = api_client.delete(date_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_if_get_request_returns_object(self, api_client, date_detail_view_url):
        obj = baker.make(CustomDate)

        response = api_client.get(date_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == obj.pk  

    def test_if_get_request_nonexistent_object_returns_404(self, api_client, date_detail_view_url):
        response = api_client.get(date_detail_view_url(99999999))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
@pytest.mark.django_db
class TestCustomDateCreateView:

    def test_if_post_request_creates_object(self, api_client, date_create_view_url):
        adv = baker.make(CustomAdvertisement, start_date="2024-1-22", end_date="2024-1-25")
        data = {     
            "date":"2024-1-22",
            "adv_id":adv.pk
        }

        response = api_client.post(date_create_view_url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomDate.objects.count() == 1

@pytest.mark.django_db
class TestCustomDateDeleteView:

    def test_if_delete_request_deletes_object(self, api_client, date_delete_view_url):
        obj = baker.make(CustomDate)
        
        response = api_client.delete(date_delete_view_url(obj.pk))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert CustomDate.objects.count() == 0

    def test_if_delete_request_nonexistent_object_returns_404(self, api_client, date_delete_view_url):
        response = api_client.delete(date_delete_view_url(9999999999))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
@pytest.mark.django_db
class TestCustomDateUpdateView:

    def test_if_put_request_updates_object(self, api_client, date_update_view_url):
        obj = baker.make(CustomDate)
        adv = baker.make(CustomAdvertisement, start_date="2024-1-22", end_date="2024-1-25")
 
        data = {     
            "date":"2024-1-22",
            "adv_id":adv.pk
        }

        response = api_client.put(date_update_view_url(obj.pk), data=data)
        assert response.status_code == status.HTTP_200_OK
        obj.refresh_from_db()
        assert obj.date == datetime.strptime("2024-1-22", "%Y-%m-%d").date()

    def test_if_patch_request_updates_object(self, api_client, date_update_view_url):
        obj = baker.make(CustomDate)
        adv = baker.make(CustomAdvertisement, start_date="2024-1-22", end_date="2024-1-25")
 
        data = {     
            "date":"2024-1-22",
            "adv_id":adv.pk
        }

        response = api_client.patch(date_update_view_url(obj.pk), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        obj.refresh_from_db()
        assert obj.date ==  datetime.strptime("2024-1-22", "%Y-%m-%d").date()
from decimal import *
import decimal
import pytest
from rest_framework import status
from model_bakery import baker
from datetime import datetime, timedelta
from CustomAdvertisement.models import CustomAdvertisement

@pytest.mark.django_db
class TestCustomAdvertisementFilterView:
    def test_if_post_request_is_status_405(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.post(advertisement_filter_lowerprice_view_url(obj.price - 1))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.put(advertisement_filter_lowerprice_view_url(obj.price - 1))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.patch(advertisement_filter_lowerprice_view_url(obj.price - 1))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.delete(advertisement_filter_lowerprice_view_url(obj.price - 1))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    
    #lower price    
    def test_if_get_request_lowerprice_returns_objects(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)

        response = api_client.get(advertisement_filter_lowerprice_view_url(obj.price))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_lowerprice_nonexistent_object(self, api_client, advertisement_filter_lowerprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_lowerprice_view_url(obj.price + 10))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
       
    #upper price 
    def test_if_get_request_upperprice_returns_objects(self, api_client, advertisement_filter_upperprice_view_url):
        obj = baker.make(CustomAdvertisement)

        response = api_client.get(advertisement_filter_upperprice_view_url(obj.price))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_upperprice_nonexistent_object(self, api_client, advertisement_filter_upperprice_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_upperprice_view_url(obj.price - 10))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
    
    #car category
    def test_if_get_request_carcategory_returns_objects(self, api_client, advertisement_filter_carcategory_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_carcategory_view_url(obj.car_category))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_carcategory_nonexistent_objects(self, api_client, advertisement_filter_carcategory_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_carcategory_view_url(obj.car_category+"x"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
        
    #car color
    def test_if_get_request_carcolor_returns_objects(self, api_client, advertisement_filter_carcolor_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_carcolor_view_url(obj.car_color))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_carcolor_nonexistent_objects(self, api_client, advertisement_filter_carcolor_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_carcolor_view_url(obj.car_color+"x"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
    
    #start date
    def test_if_get_request_startdate_returns_objects(self, api_client, advertisement_filter_startdate_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_startdate_view_url(obj.start_date))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_startdate_nonexistent_objects(self, api_client, advertisement_filter_startdate_view_url):
        obj = baker.make(CustomAdvertisement)
        start_date = obj.end_date + timedelta(days=1)
        
        response = api_client.get(advertisement_filter_startdate_view_url(start_date))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
        
    #end date
    def test_if_get_request_enddate_returns_objects(self, api_client, advertisement_filter_enddate_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_enddate_view_url(obj.end_date))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_enddate_nonexistent_objects(self, api_client, advertisement_filter_enddate_view_url):
        obj = baker.make(CustomAdvertisement)
        end_date = obj.start_date - timedelta(days=1)
        
        response = api_client.get(advertisement_filter_enddate_view_url(end_date))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0
        
    #state
    def test_if_get_request_state_returns_objects(self, api_client, advertisement_filter_state_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_state_view_url(obj.location_state))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==1
        assert response.data[0]["id"] == obj.pk  
        
    def test_if_get_request_state_nonexistent_objects(self, api_client, advertisement_filter_state_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.get(advertisement_filter_state_view_url(obj.location_state+"x"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data)==0   
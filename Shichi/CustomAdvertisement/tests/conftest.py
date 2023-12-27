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

@pytest.fixture
def advertisement_search_view_url():
    def do_advertisement_search_view_url(car_name):
        return reverse('advertisement_search')+(f'?search={car_name}')
    
    return do_advertisement_search_view_url

@pytest.fixture
def advertisement_filter_view_url():
    def do_advertisement_filter_view_url(lower_price, upper_price, car_category, car_color, start_date, end_date, state):
        url = 'advertisement_search'
        if lower_price:
            url += f'?lower_price={lower_price}'
        if upper_price:
            url += f'&?upper_price={upper_price}'
        if car_category:
            url += f'&car_category={car_category}'   
        if car_color:
            url += f'&car_color={car_color}'
        if start_date:
            url += f'&start_date={start_date}' 
        if end_date:
            url += f'&end_date={end_date}' 
        if state:
            url += f'&state={state}' 
        
        url += '/'
            
        return url
    
    return do_advertisement_filter_view_url
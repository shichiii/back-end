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
def advertisement_filter_lowerprice_view_url():
    def do_advertisement_filter_lowerprice_view_url(lower_price):
        url = reverse('advertisement_filter')
        url += f'?lower_price={lower_price}'
        return url
    
    return do_advertisement_filter_lowerprice_view_url

@pytest.fixture
def advertisement_filter_upperprice_view_url():
    def do_advertisement_filter_upperprice_view_url(upper_price):
        url = reverse('advertisement_filter')
        url += f'?upper_price={upper_price}'
        return url
    
    return do_advertisement_filter_upperprice_view_url

@pytest.fixture
def advertisement_filter_carcategory_view_url():
    def do_advertisement_filter_carcategory_view_url(car_category):
        url = reverse('advertisement_filter')
        url += f'?car_category={car_category}'
        return url
    
    return do_advertisement_filter_carcategory_view_url

@pytest.fixture
def advertisement_filter_carcolor_view_url():
    def do_advertisement_filter_carcolor_view_url(car_color):
        url = reverse('advertisement_filter')
        url += f'?car_color={car_color}'
        return url
    
    return do_advertisement_filter_carcolor_view_url

@pytest.fixture
def advertisement_filter_startdate_view_url():
    def do_advertisement_filter_startdate_view_url(start_date):
        url = reverse('advertisement_filter')
        url += f'?start_date={start_date}'
        return url
    
    return do_advertisement_filter_startdate_view_url

@pytest.fixture
def advertisement_filter_enddate_view_url():
    def do_advertisement_filter_enddate_view_url(end_date):
        url = reverse('advertisement_filter')
        url += f'?end_date={end_date}'
        return url
    
    return do_advertisement_filter_enddate_view_url

@pytest.fixture
def advertisement_filter_state_view_url():
    def do_advertisement_filter_state_view_url(state):
        url = reverse('advertisement_filter')
        url += f'?state={state}'
        return url
    
    return do_advertisement_filter_state_view_url
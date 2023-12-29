# from django.urls import reverse
# from rest_framework.test import APIClient
# import pytest
# import pytest
# from django.conf import settings

# settings.configure()

# @pytest.fixture
# def api_client():
#     return APIClient()

# @pytest.fixture
# def customCarImage_list_view_url():
#     return reverse('list')

# @pytest.fixture
# def customCarImage_detail_view_url():
#     def do_customCarImage_detail_view_url(customCarImage_id):
#         return reverse('show', kwargs={'id': customCarImage_id})
#     return do_customCarImage_detail_view_url

# @pytest.fixture
# def customCarImage_create_view_url():
#     return reverse('create')

# @pytest.fixture
# def customCarImage_delete_view_url():
#     def do_customCarImage_delete_view_url(customCarImage_id):
#         return reverse('delete', kwargs={'pk': customCarImage_id})
#     return do_customCarImage_delete_view_url

# @pytest.fixture
# def customCarImage_update_view_url():
#     def do_customCarImage_update_view_url(customCarImage_id):
#         return reverse('update', kwargs={'pk': customCarImage_id})
#     return do_customCarImage_update_view_url
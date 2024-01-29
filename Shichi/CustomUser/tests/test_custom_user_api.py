import pytest
from rest_framework import status
from model_bakery import baker
from CustomUser.models import CustomUser

@pytest.mark.django_db
class TestCustomUserViewSet:

    def test_if_post_request_is_status_405(self, api_client, user_list_view_url):
        response = api_client.post(user_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, user_list_view_url):
        response = api_client.put(user_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, user_list_view_url):
        response = api_client.patch(user_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, user_list_view_url):
        response = api_client.delete(user_list_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    # def test_if_get_request_returns_objects(self, api_client, user_list_view_url):
    #     baker.make(CustomUser, _quantity=3)
        
    #     response = api_client.get(user_list_view_url)
    #     assert response.status_code == status.HTTP_200_OK
    #     assert len(response.data) == 3 
        
# @pytest.mark.django_db
# class TestCustomUserShowView:

    # def test_if_post_request_is_status_405(self, api_client, user_detail_view_url):
    #     obj = baker.make(CustomUser)
        
    #     response = api_client.post(user_detail_view_url(obj.pk))
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # def test_if_put_request_is_status_405(self, api_client, user_detail_view_url):
    #     obj = baker.make(CustomUser)
        
    #     response = api_client.put(user_detail_view_url(obj.pk))
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # def test_if_patch_request_is_status_405(self, api_client, user_detail_view_url):
    #     obj = baker.make(CustomUser)
    #     response = api_client.patch(user_detail_view_url(obj.pk))
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

#     def test_if_delete_request_is_status_405(self, api_client, user_detail_view_url):
#         obj = baker.make(CustomUser)
        
#         response = api_client.delete(user_detail_view_url(obj.pk))
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    # def test_if_get_request_returns_object(self, api_client, user_detail_view_url):
    #     obj = baker.make(CustomUser)

    #     response = api_client.get(user_detail_view_url(obj.pk))
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["id"] == obj.pk  

#     def test_if_get_request_nonexistent_object_returns_404(self, api_client, user_detail_view_url):
#         response = api_client.get(user_detail_view_url(99999999))
#         assert response.status_code == status.HTTP_404_NOT_FOUND
        
# @pytest.mark.django_db
# class TestCustomUserCreateView:

#     def test_if_post_request_creates_object(self, api_client, user_create_view_url):
#         user = baker.make(CustomUser)  
#         api_client.force_authenticate(user=user)

#         data = {     
#             "first_name":user.first_name,
#             "last_name": user.last_name,
#             "email": user.email,
#             "password": user.password,
#         }

#         response = api_client.post(user_create_view_url, data=data, format='json')
#         assert response.status_code == status.HTTP_201_CREATED
#         assert CustomUser.objects.count() == 1

# @pytest.mark.django_db
# class TestCustomUserDeleteView:

#     def test_if_delete_request_deletes_object(self, api_client, user_delete_view_url):
#         obj = baker.make(CustomUser)
        
#         response = api_client.delete(user_delete_view_url(obj.pk))
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert CustomUser.objects.count() == 0

#     def test_if_delete_request_nonexistent_object_returns_404(self, api_client, user_delete_view_url):
#         response = api_client.delete(user_delete_view_url(9999999999))
#         assert response.status_code == status.HTTP_404_NOT_FOUND
        
# @pytest.mark.django_db
# class TestCustomUserUpdateView:

#     def test_if_put_request_updates_object(self, api_client, user_update_view_url):
#         obj = baker.make(CustomUser)
#         api_client.force_authenticate(user=obj)
 
#         data = {
#             "email": obj.email,
#             "password": obj.password,
#             "profile_image": obj.profile_image,
#             "phone_number": obj.phone_number,
#         }

#         response = api_client.put(user_update_view_url(obj.pk), data=data)
#         assert response.status_code == status.HTTP_200_OK
#         obj.refresh_from_db()
#         assert obj.car_color == "black"

#     def test_if_patch_request_updates_object(self, api_client, user_update_view_url):
#         # obj = baker.make(CustomUser)
#         user = baker.make(CustomUser)  
#         # api_client.force_authenticate(user=user)
        
#         # data = {
#         #     "car_color": "black",
#         #     "owner_id": user.pk 
#         # }

#         # response = api_client.patch(user_update_view_url(obj.pk), data=data, format='json')
#         # assert response.status_code == status.HTTP_200_OK
#         # obj.refresh_from_db()
#         # assert obj.car_color == "black"
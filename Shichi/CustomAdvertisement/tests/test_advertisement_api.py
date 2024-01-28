import pytest
from rest_framework import status
from model_bakery import baker
from CustomAdvertisement.models import CustomAdvertisement, Comment
from CustomUser.models import CustomUser

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
        
    def test_if_get_request_returns_objects(self, api_client, advertisement_list_view_url):
        baker.make(CustomAdvertisement, _quantity=3)
        
        response = api_client.get(advertisement_list_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3 
        
@pytest.mark.django_db
class TestCustomAdvertisementShowView:

    def test_if_post_request_is_status_405(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.post(advertisement_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.put(advertisement_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.patch(advertisement_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.delete(advertisement_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_if_get_request_returns_object(self, api_client, advertisement_detail_view_url):
        obj = baker.make(CustomAdvertisement)

        response = api_client.get(advertisement_detail_view_url(obj.pk))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == obj.pk  

    def test_if_get_request_nonexistent_object_returns_404(self, api_client, advertisement_detail_view_url):
        response = api_client.get(advertisement_detail_view_url(99999999))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
@pytest.mark.django_db
class TestCustomAdvertisementCreateView:

    def test_if_post_request_creates_object(self, api_client, advertisement_create_view_url):
        user = baker.make(CustomUser)  
        api_client.force_authenticate(user=user)

        data = {     
            "owner_id":user.pk,
            "start_date": "2023-11-03",
            "end_date": "2023-11-03",
            "price": "20.00",  
            "description": "nullllll",
            "car_name": "new car",
            "car_color": "black",
            "car_produced_date": "2023-12-13",
            "car_seat_count": 4,
            "car_door_count": 4,
            "car_Is_cooler": "yes",
            "car_gearbox": "manual",
            "car_fuel": "40.00",
            "car_category": "economy",
            "location_state": "Tehran",
            "location_geo_width": "35.659249",
            "location_geo_length": "51.382326"
        }

        response = api_client.post(advertisement_create_view_url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomAdvertisement.objects.count() == 1

@pytest.mark.django_db
class TestCustomAdvertisementDeleteView:

    def test_if_delete_request_deletes_object(self, api_client, advertisement_delete_view_url):
        obj = baker.make(CustomAdvertisement)
        
        response = api_client.delete(advertisement_delete_view_url(obj.pk))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert CustomAdvertisement.objects.count() == 0

    def test_if_delete_request_nonexistent_object_returns_404(self, api_client, advertisement_delete_view_url):
        response = api_client.delete(advertisement_delete_view_url(9999999999))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
@pytest.mark.django_db
class TestCustomAdvertisementUpdateView:

    def test_if_put_request_updates_object(self, api_client, advertisement_update_view_url):
        obj = baker.make(CustomAdvertisement)
        user = baker.make(CustomUser)  
        api_client.force_authenticate(user=user)
 
        data = {
            "start_date": obj.start_date,
            "end_date": obj.end_date,
            "car_color": "black",
            "car_produced_date": obj.car_produced_date,
        }

        response = api_client.put(advertisement_update_view_url(obj.pk), data=data)
        assert response.status_code == status.HTTP_200_OK
        obj.refresh_from_db()
        assert obj.car_color == "black"

    def test_if_patch_request_updates_object(self, api_client, advertisement_update_view_url):
        obj = baker.make(CustomAdvertisement)
        user = baker.make(CustomUser)  
        api_client.force_authenticate(user=user)
        
        data = {
            "car_color": "black",
            "owner_id": user.pk 
        }

        response = api_client.patch(advertisement_update_view_url(obj.pk), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        obj.refresh_from_db()
        assert obj.car_color == "black"

@pytest.mark.django_db
class TestCustomAdvertisementUserView:
    def test_if_post_request_is_status_405(self, api_client, advertisement_user_view_url):
        response = api_client.post(advertisement_user_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_put_request_is_status_405(self, api_client, advertisement_user_view_url):
        response = api_client.put(advertisement_user_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_patch_request_is_status_405(self, api_client, advertisement_user_view_url):
        response = api_client.patch(advertisement_user_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_if_delete_request_is_status_405(self, api_client, advertisement_user_view_url):
        response = api_client.delete(advertisement_user_view_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
    def test_if_get_request_returns_objects(self, api_client, advertisement_user_view_url):
        baker.make(CustomAdvertisement, _quantity=2)
        user = baker.make(CustomUser) 
        api_client.force_authenticate(user=user)
        baker.make(CustomAdvertisement, owner_id=user.pk, _quantity=3, )
        
        response = api_client.get(advertisement_user_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3 
        
    def test_if_get_request_nonexistent_object_returns_404(self, api_client, advertisement_user_view_url):
        user = baker.make(CustomUser) 
        baker.make(CustomAdvertisement, owner_id=user.pk, _quantity=3, )
        
        response = api_client.get(advertisement_user_view_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0 
        
        
        
        
        
        
        
        
        
        
        
        
        

        
# from django.core.files.uploadedfile import SimpleUploadedFile
# import pytest

# @pytest.mark.django_db
# class TestCommentCreateView:

#     def test_if_post_request_creates_object(self, api_client, comment_create_view_url):
#         # dummy_file = SimpleUploadedFile(
#         #     name='test_image.jpg',
#         #     content=open('./back-end/Shichi/CustomAdvertisement/tests/Image.jpg', 'rb').read(),
#         #     content_type='image/jpeg'
#         # )
#         user = baker.make(CustomUser)  
#         # user = baker.make(CustomUser, profile_image=dummy_file)  
#         api_client.force_authenticate(user=user)
#         adv = baker.make(CustomAdvertisement)
#         data = {     
#             "user_id": user.pk,
#             "adv": adv.pk,  
#             "text": "this is just for test"
#         }
#         response = api_client.post(comment_create_view_url, data=data)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Comment.objects.count() == 1

# @pytest.mark.django_db
# class TestCustomAdvertisementDeleteView:

#     def test_if_delete_request_deletes_object(self, api_client, comment_delete_view_url):
#         obj = baker.make(CustomAdvertisement)
        
#         response = api_client.delete(comment_delete_view_url(obj.pk))
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert Comment.objects.count() == 0

#     def test_if_delete_request_nonexistent_object_returns_404(self, api_client, comment_delete_view_url):
#         response = api_client.delete(comment_delete_view_url(9999999999))
#         assert response.status_code == status.HTTP_404_NOT_FOUND
        
# @pytest.mark.django_db
# class TestCustomAdvertisementUpdateView:

#     def test_if_put_request_updates_object(self, api_client, comment_update_view_url):
#         obj = baker.make(Comment)
#         user = baker.make(CustomUser)  
#         api_client.force_authenticate(user=user)
 
#         data = {
#             "user_id" : user.pk,
#             "created_date": obj.created_date,
#             "text": obj.text,
#         }

#         response = api_client.put(comment_update_view_url(obj.pk), data=data)
#         assert response.status_code == status.HTTP_200_OK
#         obj.refresh_from_db()
#         assert obj.car_color == "black"

#     def test_if_patch_request_updates_object(self, api_client, comment_update_view_url):
#         obj = baker.make(Comment)
#         user = baker.make(CustomUser)  
#         api_client.force_authenticate(user=user)
        
#         data = {
#             "text": "i change this line.",
#             "owner_id": user.pk 
#         }

#         response = api_client.patch(comment_update_view_url(obj.pk), data=data, format='json')
#         assert response.status_code == status.HTTP_200_OK
#         obj.refresh_from_db()
#         assert obj.text == "i change this line."

# @pytest.mark.django_db
# class TestCustomAdvertisementUserView:
#     def test_if_post_request_is_status_405(self, api_client, comment_user_view_url):
#         response = api_client.post(comment_user_view_url)
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

#     def test_if_put_request_is_status_405(self, api_client, comment_user_view_url):
#         response = api_client.put(comment_user_view_url)
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

#     def test_if_patch_request_is_status_405(self, api_client, comment_user_view_url):
#         response = api_client.patch(comment_user_view_url)
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

#     def test_if_delete_request_is_status_405(self, api_client, comment_user_view_url):
#         response = api_client.delete(comment_user_view_url)
#         assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        
#     def test_if_get_request_returns_objects(self, api_client, comment_user_view_url):
#         baker.make(Comment, _quantity=2)
#         user = baker.make(CustomUser) 
#         api_client.force_authenticate(user=user)
#         baker.make(Comment, owner_id=user.pk, _quantity=3, )
        
#         response = api_client.get(comment_user_view_url)
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 3 
        
#     def test_if_get_request_nonexistent_object_returns_404(self, api_client, comment_user_view_url):
#         user = baker.make(CustomUser) 
#         baker.make(Comment, owner_id=user.pk, _quantity=3, )
        
#         response = api_client.get(comment_user_view_url)
#         assert response.status_code == status.HTTP_200_OK
#         assert len(response.data) == 0 
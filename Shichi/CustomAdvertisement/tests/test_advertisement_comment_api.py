import pytest
from rest_framework import status
from model_bakery import baker
from CustomAdvertisement.models import CustomAdvertisement, Comment
from CustomUser.models import CustomUser    
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_create_comment():
    user = baker.make(CustomUser)
    adv = baker.make(CustomAdvertisement)
    comment_data = {
        'user_id': user.id,
        'adv': adv,
        'text': 'Sample comment text',
    }
    comment = Comment.objects.create(**comment_data)
    assert comment is not None
    assert comment.user_id == user.id
    assert comment.adv == adv
    assert comment.text == 'Sample comment text'
    
from CustomAdvertisement.serializers import CommentSerializer

@pytest.mark.django_db
def test_comment_serializer_with_invalid_data():
    # Create test instances for necessary relations
    user = baker.make(CustomUser)
    adv = baker.make(CustomAdvertisement)

    invalid_data = [
        # Invalid because 'user_id' is missing
        {'adv': adv, 'text': 'Sample comment text'},  
        # Invalid because 'adv' is missing
        {'user_id': user.id, 'text': 'Sample comment text'},  
        # Invalid because 'text' is missing
        {'user_id': user.id, 'adv': adv},  
        # Invalid because 'user_id' is incorrect (not existing)
        {'user_id': 9999, 'adv': adv, 'text': 'Sample alaki text'},  
        # Invalid because 'adv' is incorrect (not existing)
        {'user_id': user.id, 'adv': 999999, 'text': 'Sample comment text'},
    ]

    for data in invalid_data:
        serializer = CommentSerializer(data=data)
        assert not serializer.is_valid()
        
# @pytest.mark.django_db
# def test_update_comment(comment_update_view_url, api_client):
#     user = baker.make(CustomUser)
#     adv = baker.make(CustomAdvertisement)
#     comment = baker.make(Comment, user_id=user.id, adv=adv, text='Sample comment text')
    
#     api_client.force_authenticate(user=user)
#     updated_data = {
#         'text': 'Updated comment text'
#     }
#     url = comment_update_view_url(comment.id)
#     response = api_client.put(url, updated_data, format='json')
#     assert response.status_code == status.HTTP_200_OK
#     comment.refresh_from_db()
#     assert comment.text == updated_data['text']
#     api_client.logout()

  
@pytest.mark.django_db
class TestCustomAdvertisementDeleteView:

    def test_if_delete_request_deletes_object(self, api_client, comment_delete_view_url):
        obj = baker.make(Comment)
        
        response = api_client.delete(comment_delete_view_url(obj.pk))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Comment.objects.count() == 0

    def test_if_delete_request_nonexistent_object_returns_404(self, api_client, comment_delete_view_url):
        response = api_client.delete(comment_delete_view_url(9999999999))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
# @pytest.mark.django_db

# def test_if_put_request_updates_object(self, api_client, comment_update_view_url):
#     obj = baker.make(Comment)
#     user = baker.make(CustomUser)  
#     adv = baker.make(CustomAdvertisement)  
#     api_client.force_authenticate(user=user)

#     data = {
#         "user_id" : user.pk,
#         "adv": adv,
#         "text": obj.text,
#     }
#     response = api_client.put(comment_update_view_url(obj.pk), data=data)
#     assert response.status_code == status.HTTP_200_OK
#     obj.refresh_from_db()
#     assert obj.text == "black"

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
# def test_delete_comment(comment_delete_url, api_client):
#     user = baker.make(CustomUser)
#     adv = baker.make(CustomAdvertisement)
#     comment = baker.make(Comment, user_id=user.id, adv=adv, text = 'nothing1')
#     api_client.force_authenticate(user=user)
#     url = comment_delete_url(comment.id)
#     response = api_client.delete(url)
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     assert not Comment.objects.filter(id=comment.id).exists()
#     api_client.logout()
    

# @pytest.mark.django_db
# class TestCommentAdvertisementView:
#     def test_if_post_request_is_status_405(self, api_client, comment_detail_view_url):
#         response = api_client.post(comment_detail_view_url)
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
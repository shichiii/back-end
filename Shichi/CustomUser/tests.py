from django.test import TestCase
import json
from .models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient, APITestCase
from Shichi.urls import *
from django.contrib.auth import get_user_model
from phonenumbers import parse, PhoneNumberFormat
from phonenumber_field.phonenumber import PhoneNumber

# 5 tests
class UserTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(first_name="test1", last_name = "test2", email = "test@gmail.com", password="Ab654321")
        self.user.is_active = True
        self.user.save()
    
    def test_login_success(self):
        url = reverse('user:login')
        data = {"email" : "test@gmail.com", "password": "Ab654321"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_login_failure_password(self):
        url = reverse("user:login")
        data = {"password": "4321"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_signup_failure_repeatetive_email(self):
        CustomUser.objects.create_user(
            first_name="test1", last_name = "test2", password="Ab654321", email="test@eamil.com"
        )
        url = reverse("user:signup")
        data = {
            "first_name": "test",
            "last_name": "test",
            "password": "Ab654321",
            "email": "test@eamil.com",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        url = reverse("user:login")
        response = self.client.post(
            url, {"email": "test@gmail.com", "password": "Ab654321"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("refresh" in response.data)
        self.assertTrue("access" in response.data)
         
    def login(self, email, password):
        url = reverse('user:login')
        data = json.dumps({'email': email, 'password': password})
        response = self.client.post(url, data, content_type='application/json')
        if response.status_code == status.HTTP_200_OK:
            access_token = response.data['access']
            return access_token
        else:
            return "incorrect"
        
    def post_login(self, data, user):
        token = self.login(self.user.email, 'mo@gmail.com')
        self.client.credentials(Authorization='Bearer' + token)  
        response = self.client.post(self.url, data=data)
        return response.data  
          
    def test_update_custom_user(self):
        token = self.login(self.user.email, "Ab654321")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('user:update', kwargs={'pk': self.user.pk})
        data = {
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
            'phone_number': '+12345678901',
            
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.data['phone_number'], data['phone_number'])
        return response.data

    def test_update_custom_user_permission_denied(self):
        token = self.login(self.user.email, "Ab654321")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('user:update', kwargs={'pk': self.user.pk + 1})
        data = {
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
            'phone_number': '+12345678901',
            
        }
        response = self.client.put(url, data, format='json')   
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        return response.data
    
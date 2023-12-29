from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import SetPasswordResetSerializer, UpdateCustomUserWalletSerializer, CustomUserSerializer, LoginSignupCustomUserSerializer, UpdateCustomUserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsEditUser]

class CreateCustomUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSignupCustomUserSerializer
    # permission_classes = [IsEditUser]

    def perform_create(self, serializer):
        serializer.save(password = make_password(self.request.data.get('password')))


class MyCustomUser(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            print(user_id, "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPp")
            user = CustomUser.objects.get(id=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
class ShowCustomUser(generics.RetrieveAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'

class UpdateCustomUser(generics.UpdateAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = UpdateCustomUserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user != instance:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteCustomUser(generics.DestroyAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_destroy(self, instance):
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user != instance:
            return Response({'error': 'User Not Allowed.'}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
from .serializers import PasswordResetSerializer   
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail  # Import send_mail for sending the email.

class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            user =CustomUser.objects.get(email=email)  

            token = default_token_generator.make_token(user)
            serializer.token = token

            # for generating the reset URL.
            current_site = get_current_site(request)

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # reset_url = f"http://{current_site.domain}/user/password-reset-confirm/{uidb64}/{token}/"
            reset_url = f"Localhost:3000/reset/{token}/"
            print(f"Reset URL: {reset_url}")

            subject = "Password Reset Request"
            message = f"Please click the following link to reset your password:\n{reset_url}"
            from_email = "shichiiii777@example.com"  # Replace with your email address.
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from Payments.views import go_to_gateway_view
class PasswordResetConfirmView(APIView):
    serializer_class = SetPasswordResetSerializer
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                # valid; allow the user to reset the password
                new_password = request.data.get('new_password')
                user.password = make_password(new_password)
                user.save()
                return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)
 
    
class RequestForWallet(generics.UpdateAPIView):
    serializer_class = UpdateCustomUserWalletSerializer
    queryset = CustomUser.objects.all()

    def update(self, instance, *args, **kwargs):
        email = self.request.user
        id = kwargs.get('pk')
        user = CustomUser.objects.get(email=email)
        if user.id == id:
            ser = UpdateCustomUserWalletSerializer(data=self.request.data)
            if ser.is_valid():
                wallet = ser.validated_data['wallet']
                res = go_to_gateway_view(self.request, user.email, wallet)
                return Response(str(res.url), status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
            
            

from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .models import CustomUser, Wallet
from .serializers import CustomUserSerializer, LoginSignupCustomUserSerializer, UpdateCustomUserSerializer
from .serializers import WalletSerializer
from django.contrib.auth.hashers import make_password, check_password

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

    def perform_update(self, serializer):
        instance = serializer.instance
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user != instance:
            print(instance , user)
            return Response({'error': 'User Not Allowed.'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

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
            reset_url = f"http://{current_site.domain}/user/password-reset-confirm/{uidb64}/{token}/"

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

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                # valid; allow the user to reset the password
                new_password = request.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)
 

class WalletListView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletCreateView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletUpdateView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletDeleteView(generics.DestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    
    
# import logging
# from django.urls import reverse
# # from azbankgateways import bankfactories, models as bank_models, default_settings as settings
# # from azbankgateways.exceptions import AZBankGatewaysException
# from django.http import HttpResponse, Http404


# # def go_to_gateway_view(request):
# #     amount = 10000
# #     # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
# #     user_mobile_number = '+989112521234'  # اختیاری
# #     factory = bankfactories.BankFactory()
# #     try:
# #         # bank = factory.auto_create() # or 
# #         bank = factory.create(bank_models.BankType.IDPAY) 
# #         bank.set_request(request)
# #         bank.set_amount(amount)
# #         bank.set_client_callback_url('callback-gateway/')  # reverse...
# #         bank.set_mobile_number(user_mobile_number)  # اختیاری
# #         bank_record = bank.ready()
# #         return bank.redirect_gateway()
#     # except AZBankGatewaysException as e:
#     #     logging.critical(e)
#     #     # TODO: redirect to failed page.
#     #     raise e


# def callback_gateway_view(request):
#     tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
#     if not tracking_code:
#         logging.debug("این لینک معتبر نیست.")
#         raise Http404

#     try:
#         bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
#     except bank_models.Bank.DoesNotExist:
#         logging.debug("این لینک معتبر نیست.")
#         raise Http404

#     # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
#     if bank_record.is_success:
#         # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
#         # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
#         return HttpResponse("پرداخت با موفقیت انجام شد.")

#     # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
#     return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
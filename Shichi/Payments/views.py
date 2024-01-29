from django.shortcuts import render
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from CustomUser.models import CustomUser
from Payments.models import PaymentLog
from Payments.serializers import PaymentLogSerializer
from rest_framework import generics, permissions, viewsets, status

# Create your views here.
def go_to_gateway_view(request, email, amount=50000):
    user_mobile_number = '+989112521234' 
    factory = bankfactories.BankFactory()
    try:
        # bank = factory.auto_create() # or 
        bank = factory.create(bank_models.BankType.ZARINPAL) 
        bank.set_request(request)
        bank.set_amount(amount)
        bank.set_client_callback_url(reverse('callback-gateway'))  # reverse...
        bank.set_mobile_number(user_mobile_number)  # اختیاری
        bank_record = bank.ready()
        payment = PaymentLog(user_email = email, money = amount, bank_code = str(bank_record).split('-')[1])
        print(payment.user_email)
        payment.save()
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        raise e

def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404
    if bank_record.is_success:
        payment = PaymentLog.objects.get(bank_code = tracking_code)
        payment.was_successful = True
        payment.save()
        if payment is not None:
            user = CustomUser.objects.get(email = payment.user_email)
            user.wallet = user.wallet+payment.money
            user.save()
            payment.is_added = True
            payment.save()
        return HttpResponse("Successfull")
        
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentLog.objects.all()
    serializer_class = PaymentLogSerializer
    # permission_classes = [IsEditUser]

class DeletePayment(generics.DestroyAPIView):
    # permission_classes = [IsEditUser]
    queryset = PaymentLog.objects.all()
    serializer_class = PaymentLogSerializer
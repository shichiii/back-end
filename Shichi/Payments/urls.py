from azbankgateways.urls import az_bank_gateways_urls
from .views import go_to_gateway_view, callback_gateway_view
from django.urls import path


# app_name = "user"

urlpatterns = [    
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view),
    path('callback-gateway/', callback_gateway_view, name = 'callback-gateway'),
]
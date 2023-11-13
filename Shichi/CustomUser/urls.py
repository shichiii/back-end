from django.urls import path, include
from .views import CustomUserViewSet, CreateCustomUser, MyCustomUser, ShowCustomUser, UpdateCustomUser, DeleteCustomUser
from .views import PasswordResetView, PasswordResetConfirmView
from .views import WalletListView, WalletCreateView, WalletUpdateView, WalletDeleteView
from .views import go_to_gateway_view, callback_gateway_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib.auth.views import (
    PasswordResetDoneView, 
    # PasswordResetConfirmView,
    # PasswordResetCompleteView
)

app_name = "user"
from azbankgateways.urls import az_bank_gateways_urls

urlpatterns = [
    path('myshow/', MyCustomUser.as_view(), name='myshow'),
    path('show/<int:id>/', ShowCustomUser.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateCustomUser.as_view(), name='signup'),
    path('update/<int:pk>/', UpdateCustomUser.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCustomUser.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/', PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    
    path('WalletList/', WalletListView.as_view(), name='Walletlist'),
    path('WalletCreate/', WalletCreateView.as_view(), name='WalletCreate'),
    path('WalletUpdate/<int:pk>/', WalletUpdateView.as_view(), name='WalletUpdate'),
    # path('WalletDelete/<int:pk>/', DeleteCustomUser.as_view(), name='WalletDelete'),
    # path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view),
    path('callback-gateway/', callback_gateway_view),
]


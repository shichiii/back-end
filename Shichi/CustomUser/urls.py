from django.urls import path, include
from .views import CustomUserViewSet, CreateCustomUser, MyCustomUser, ShowCustomUser, UpdateCustomUser
from .views import PasswordResetView, PasswordResetConfirmView, RequestForWallet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib.auth.views import (
    PasswordResetDoneView, 
)

app_name = "user"
from .views import delete_custom_user
urlpatterns = [
    path('myshow/', MyCustomUser.as_view(), name='myshow'),
    path('show/<int:id>/', ShowCustomUser.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateCustomUser.as_view(), name='signup'),
    path('update/<int:pk>/', UpdateCustomUser.as_view(), name='update'),
    path('updatewallet/<int:pk>/', RequestForWallet.as_view(), name='updateWallet'),
    path('delete/<int:user_id>/', delete_custom_user, name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/', PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]


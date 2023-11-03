from django.urls import path, include
from .views import CustomUserViewSet, CreateCustomUser, MyCustomUser, ShowCustomUser, UpdateCustomUser, DeleteCustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.views import (
    # LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# from allauth.account.views import (
#     PasswordResetView, 
#     PasswordResetDoneView, 
#     PasswordResetConfirmView, 
#     PasswordResetCompleteView, 
#     EmailVerificationSentView, 
#     ConfirmEmailView
# )


urlpatterns = [
    path('myshow/', MyCustomUser.as_view(), name='myshow'),
    path('show/<int:id>/', ShowCustomUser.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateCustomUser.as_view(), name='signup'),
    path('update/<int:pk>/', UpdateCustomUser.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCustomUser.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/', PasswordResetView.as_view(),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # path('accounts/', include('allauth.urls')),
    # path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    # path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    # path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='account_reset_password_confirm'),
    # path('accounts/password/done/', PasswordResetCompleteView.as_view(), name='account_reset_password_complete'),
    # path('accounts/email/sent/', EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    # path('accounts/confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
]


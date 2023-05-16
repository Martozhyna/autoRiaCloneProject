from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ActivateUserView,
    AuthMeView,
    AuthNewPasswordSendView,
    AuthPremiumAccountActivateView,
    AuthPremiumAccountRequestView,
    AuthRecoveryPasswordView,
    AuthRegisterView,
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/me', AuthMeView.as_view(), name='auth_show_me'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate_user'),
    path('/recovery_password', AuthRecoveryPasswordView.as_view(), name='auth_recovery_password'),
    path('/recovery_password/<str:token>', AuthNewPasswordSendView.as_view(), name='auth_new_password_send'),
    path('/premium_add', AuthPremiumAccountRequestView.as_view(), name='auth_premium_request'),
    path('/premium_add/<str:token>', AuthPremiumAccountActivateView.as_view(), name='auth_premium_activate')

]

from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView, AuthMeView, AuthRegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/me', AuthMeView.as_view(), name='auth_show_me'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate_user')

]

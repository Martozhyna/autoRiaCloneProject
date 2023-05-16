from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, PremiumAddToken, RecoveryPasswordToken

from apps.auth.serializers import CreditCardDetails, EmailSerializer, PasswordSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class AuthMeView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self):
        return self.request.user


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AuthRecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=data['email'])
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)


class AuthNewPasswordSendView(GenericAPIView):
    permission_classes = (AllowAny,)

    @atomic
    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: User = JWTService.validate_token(token, RecoveryPasswordToken)
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(data['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)


class AuthPremiumAccountRequestView(GenericAPIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CreditCardDetails(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=data['email'])
        if not user.is_seller:
            return Response('if you want buy premium account you must be seller')
        EmailService.premium_add(user)
        return Response(status=status.HTTP_200_OK)


class AuthPremiumAccountActivateView(GenericAPIView):
    @atomic
    def get(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.validate_token(token, PremiumAddToken)
        if not user.is_seller:
            return Response('if you want buy premium account you must be seller')
        user.is_premium = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


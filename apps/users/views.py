from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions.is_superuser import IsSuperuser

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


# список усіх користувачів
class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperuser, )

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


# список машин конкретного юзера
class UserCarListView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user.cars, many=True)
        print(self.request.user.id)
        print(self.request.data)
        print(kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToAdmin(GenericAPIView):
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()  # витягаємо юзера по pk

        if user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminToUser(GenericAPIView):
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not self.request.user.is_staff or (user.is_staff and not self.request.user.is_superuser):
            return Response('permission denied', status.HTTP_403_FORBIDDEN)

        if not user.is_active:
            return Response(status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        # if (self.request.user.is_staff and  not self.request.user.is_superuser and user.is_staff) :
        if not self.request.user.is_staff or (user.is_staff and not self.request.user.is_superuser):
            return Response('permission denied', status.HTTP_403_FORBIDDEN)

        if user.is_active:
            return Response(status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

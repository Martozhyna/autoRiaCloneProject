from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


# список усіх користувачів
class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


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

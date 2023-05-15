from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import CarModel, CarPhotoModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


# перегляд машин (для всіх)
class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)


# створення машин (юзер що створив = залогінений юзер), як тільки створене оголошоння юзер стає продавцем
class CarCreateView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        user = self.request.user
        user.is_seller = True
        user.save()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddPhotosView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)


class CarPhotoDeleteView(DestroyAPIView):
    queryset = CarPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)

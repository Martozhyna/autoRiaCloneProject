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

from core.permissions.is_premium import IsPremium

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel, CarPhotoModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


# перегляд машин (для всіх)
class CarListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    # filterset_class = CarFilter


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


class CarAveragePriceInUkraineView(ListAPIView):
    permission_classes = (IsPremium,)
    filterset_class = CarFilter

    def get(self, request, *args, **kwargs):
        # cars = CarModel.objects.get_cars_by_auto_park_id('Volvo')
        cars = CarModel.objects.all()
        params_dict = self.request.query_params.dict()
        # serializer = CarSerializer(instance=cars, many=True)
        if 'brand' in params_dict:
            qs = cars.filter(brand__istartswith=params_dict['brand'])
            prices = qs.values('price')
            prices_list = []
            for price in prices:
                for key in price:
                    prices_list.append(price[key])
            average_price = sum(prices_list) / len(prices_list)
            return Response(average_price)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CarAveragePriceInCityView(ListAPIView):
    permission_classes = (IsPremium,)
    filterset_class = CarFilter

    def get(self, request, *args, **kwargs):
        cars = CarModel.objects.all()
        params_dict = self.request.query_params.dict()
        if 'brand' in params_dict and 'city_of_sale' in params_dict:
            qs = cars.filter(brand__istartswith=params_dict['brand']) \
                .filter(city_of_sale__istartswith=params_dict['city_of_sale'])
            prices = qs.values('price')
            prices_list = []
            for price in prices:
                for key in price:
                    prices_list.append(price[key])
            average_price = sum(prices_list) / len(prices_list)
            return Response(average_price)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

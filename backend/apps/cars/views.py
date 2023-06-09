from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.is_premium import IsPremium

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel, CarPhotoModel
from apps.cars.serializers import (
    CarBrandProfinityFilterSerializer,
    CarCityProfinityFilterSerializer,
    CarModelProfinityFilterSerializer,
    CarPhotoSerializer,
    CarSerializer,
    CarViewSerializer,
)


# перегляд машин (для всіх)
class CarListView(ListAPIView):
    """
      Get all cars
    """
    permission_classes = (AllowAny,)
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter


class CarCreateView(GenericAPIView):
    """
       Car create
    """
    queryset = CarModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        user = self.request.user
        user.is_seller = True
        user.save()

    def post(self, serializer):

        data = self.request.data
        price = data['price'].strip('$')
        data.price = int(data['price'])

        brand_profinity = CarBrandProfinityFilterSerializer(data=data)
        model_profinity = CarModelProfinityFilterSerializer(data=data)
        city_profinity = CarCityProfinityFilterSerializer(data=data)

        if not brand_profinity.is_valid() and not model_profinity.is_valid() and not city_profinity.is_valid():

            serializer = CarSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user, is_visible=True)
            user = self.request.user

            if user.is_seller and not user.is_premium and not user.is_superuser:
                return Response('in order to post more ads you should purchase a premium subscription')

            else:
                user.is_seller = True
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response('the fields cannot contain obscene words', status=status.HTTP_400_BAD_REQUEST)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
       Car retrieve update destroy
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        car = self.get_object()
        car.views += 1
        print(car.views)
        serializer = CarSerializer(car)
        car.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarAddPhotosView(GenericAPIView):
    """
      Add cars photo
    """
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
    """
      Delete cars photo
    """
    queryset = CarPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)


class CarAveragePriceInUkraineView(ListAPIView):
    """
      Get average price in Ukraine
    """
    permission_classes = (IsPremium,)

    def get(self, request, *args, **kwargs):
        cars = CarModel.objects.all()
        params_dict = self.request.query_params.dict()

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
    """
       Get average price in city
    """
    permission_classes = (IsPremium,)

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


class CarListWithNumberOfView(GenericAPIView):
    """
       Get numbers of view
    """
    queryset = CarModel.objects.all()
    permission_classes = (IsPremium,)

    def get(self, *args, **kwargs):
        car = self.get_object()
        serializer = CarViewSerializer(car)
        car.save()
        return Response(car.views, status=status.HTTP_200_OK)

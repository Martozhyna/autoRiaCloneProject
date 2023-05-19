from django.urls import path

from .views import (
    CarAddPhotosView,
    CarAveragePriceInCityView,
    CarAveragePriceInUkraineView,
    CarCreateView,
    CarListView,
    CarListWithNumberOfView,
    CarPhotoDeleteView,
    CarRetrieveUpdateDestroyView,
)

urlpatterns = [
   path('', CarListView.as_view(), name='cars_list_view'),
   path('/create', CarCreateView.as_view(), name='cars_create'),
   path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
   path('/<int:pk>/view', CarListWithNumberOfView.as_view(), name='cars_numbers_of_view'),
   path('/<int:pk>/add_photo', CarAddPhotosView.as_view(), name='cars_photo_add'),
   path('/<int:pk>/delete_photo', CarPhotoDeleteView.as_view(), name='cars_photo_delete'),
   path('/average_price', CarAveragePriceInUkraineView.as_view(), name='cars_average_price'),
   path('/average_price/city', CarAveragePriceInCityView.as_view(), name='cars_average_price_in_city')

]
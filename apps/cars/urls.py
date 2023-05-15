from django.urls import path

from .views import CarAddPhotosView, CarCreateView, CarListView, CarPhotoDeleteView, CarRetrieveUpdateDestroyView

urlpatterns = [
   path('', CarListView.as_view(), name='cars_list_view'),
   path('/create', CarCreateView.as_view(), name='cars_create'),
   path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
   path('/<int:pk>/add_photo', CarAddPhotosView.as_view(), name='cars_photo_add'),
   path('/<int:pk>/delete_photo', CarPhotoDeleteView.as_view(), name='cars_photo_delete'),

]
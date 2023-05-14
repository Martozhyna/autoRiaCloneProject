from django.urls import path

from .views import CarCreateView, CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
   path('', CarListView.as_view(), name='cars_list_view'),
   path('/create', CarCreateView.as_view(), name='cars_create'),
   path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy')

]
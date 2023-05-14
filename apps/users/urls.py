from django.urls import path

from .views import UserCarListView, UserListView

urlpatterns = [
   path('', UserListView.as_view(), name='users_list_view'),
   path('/<int:pk>/cars', UserCarListView.as_view(), name='users_car_list_view')


]
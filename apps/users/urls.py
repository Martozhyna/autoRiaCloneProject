from django.urls import path

from .views import AdminToUser, UserBlockView, UserCarListView, UserListView, UserToAdmin, UserUnBlockView

urlpatterns = [
   path('', UserListView.as_view(), name='users_list_view'),
   path('/<int:pk>/cars', UserCarListView.as_view(), name='users_car_list_view'),
   path('/<int:pk>/to_admin', UserToAdmin.as_view(), name='users_to_admin'),
   path('/<int:pk>/to_user', AdminToUser.as_view(), name='admin_to_user'),
   path('/<int:pk>/block', UserBlockView.as_view(), name='users_block'),
   path('/<int:pk>/unblock', UserUnBlockView.as_view(), name='users_unblock'),



]
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


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




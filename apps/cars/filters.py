from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    model_start = filters.CharFilter(field_name='model', lookup_expr='istartswith')

    class Meta:
        model = CarModel
        fields = ('brand_start','model_start', )

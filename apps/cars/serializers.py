from rest_framework import serializers

from core.dataclasses.seller_dataclass import Seller

from apps.cars.models import CarModel


class SellerRelatedFieldSerializer(serializers.RelatedField):

    def to_representation(self, value: Seller):
        return {'id': value.id, 'email': value.email}


class CarSerializer(serializers.ModelSerializer):
    user = SellerRelatedFieldSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = 'id', 'brand', 'model', 'city_of_sale', 'year', 'price', 'user'
        # read_only_fields = ('seller',)

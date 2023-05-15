from rest_framework import serializers

from core.dataclasses.seller_dataclass import Seller

from apps.cars.models import CarModel, CarPhotoModel


class SellerRelatedFieldSerializer(serializers.RelatedField):

    def to_representation(self, value: Seller):
        return {'id': value.id, 'email': value.email}


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)

    def to_representation(self, instance):
        return instance.photo.url


class CarSerializer(serializers.ModelSerializer):
    user = SellerRelatedFieldSerializer(read_only=True)
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = 'id', 'brand', 'model', 'city_of_sale', 'year', 'price', 'photos', 'user'

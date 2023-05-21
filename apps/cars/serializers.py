from django.core import validators as V

from rest_framework import serializers

from core.dataclasses.seller_dataclass import Seller
from core.enums.regex_enum import RegEx

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
        fields = ('id', 'brand', 'model', 'city_of_sale', 'year', 'price', 'is_visible', 'photos', 'user',)



class CarBrandProfinityFilterSerializer(serializers.Serializer):
    brand = serializers.CharField(
        validators=[V.RegexValidator(RegEx.PROFANITY_FILTER.pattern, RegEx.PROFANITY_FILTER.msg)])


class CarModelProfinityFilterSerializer(serializers.Serializer):
    model = serializers.CharField(
        validators=[V.RegexValidator(RegEx.PROFANITY_FILTER.pattern, RegEx.PROFANITY_FILTER.msg)])


class CarCityProfinityFilterSerializer(serializers.Serializer):
    city_of_sale = serializers.CharField(
        validators=[V.RegexValidator(RegEx.PROFANITY_FILTER.pattern, RegEx.PROFANITY_FILTER.msg)])


class CarViewSerializer(serializers.ModelSerializer):
    user = SellerRelatedFieldSerializer(read_only=True)
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = 'id', 'brand', 'model', 'city_of_sale', 'year', 'price', 'is_visible', 'photos', 'user', 'views',

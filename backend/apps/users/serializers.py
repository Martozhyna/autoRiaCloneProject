from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from core.services.email_service import EmailService

from apps.cars.serializers import CarSerializer
from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'user_photo')


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True)
    # auto_parks = AutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_seller', 'is_premium', 'is_superuser', 'last_login',
            'created_at',
            'updated_at', 'profile', 'cars',
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'is_seller', 'is_premium', 'last_login',
                            'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register_email(user)
        return user

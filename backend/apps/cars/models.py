from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from djmoney.contrib.exchange.models import convert_money
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.money import Money

from core.enums.regex_enum import RegEx
from core.services.uppload_car_service import upload_to

# from apps.cars.managers import CarManager
from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel = get_user_model()


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    city_of_sale = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField()
    price = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
    is_visible = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    # auto_park = models.ForeignKey(AutoParkModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

    # objects = CarManager.as_manager()


# print(CarModel.objects.filter(auto_park_id=0))


class CarPhotoModel(models.Model):
    class Meta:
        db_table = 'cars_photo'

    photo = models.ImageField(upload_to=upload_to, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photos')




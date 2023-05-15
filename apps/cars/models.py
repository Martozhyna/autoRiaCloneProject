from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.services.uppload_car_service import upload_to

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel = get_user_model()


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    city_of_sale = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to=upload_to, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
    created_add = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

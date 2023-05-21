from django.contrib.auth import get_user_model
from django.core import validators as V

from rest_framework import serializers

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CreditCardDetails(serializers.Serializer):
    email = serializers.EmailField()
    card_number = serializers.IntegerField(
        validators=[V.RegexValidator(RegEx.CARD_NUMBER.pattern, RegEx.CARD_NUMBER.msg)])


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)
from django.core import validators as V

from rest_framework import serializers

from core.enums.regex_enum import RegEx


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CreditCardDetails(serializers.Serializer):
    email = serializers.EmailField()
    card_number = serializers.IntegerField(validators=[V.RegexValidator(RegEx.CARD_NUMBER.pattern, RegEx.CARD_NUMBER.msg)])

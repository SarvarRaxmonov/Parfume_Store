from django.core import signing
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.cache import CacheTypes
from apps.user.models.users import User


class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone_number"]

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(f"A user with the phone number {phone_number} already exists.")
        return phone_number


class VerificationRegistrationCodeSerializer(SendCodeSerializer):  # noqa
    code = serializers.CharField()
    session = serializers.CharField()

    class Meta(SendCodeSerializer.Meta):  # noqa
        fields = SendCodeSerializer.Meta.fields + ["code", "session"]  # noqa

    def validate(self, attrs):
        print(attrs)
        return attrs


class RegisterUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "first_name", "phone_number", "password", "token")


    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data

    def validate(self, attrs):
        phone_data = attrs.pop("phone_number")
        signer = signing.TimestampSigner()
        phone_data = signer.unsign_object(phone_data, max_age=600)
        if phone_data.get("type") != CacheTypes.registration_sms_verification:
            raise ValidationError(_("Wrong type!"))
        attrs["phone_number"] = phone_data.get("phone")
        return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise ValidationError(str(e))
        return user


class RecoveryCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This user does not exists. ")
        return attrs

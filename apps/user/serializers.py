from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models.users import User


class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "phone_number")

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(f"A user with the phone number {phone_number} already exists.")
        return phone_number


class VerificationRegistrationCodeSerializer(SendCodeSerializer):
    code = serializers.CharField()
    session = serializers.CharField()

    class Meta(SendCodeSerializer.Meta):  # noqa
        fields = SendCodeSerializer.Meta.fields + ("code", "session")  # noqa

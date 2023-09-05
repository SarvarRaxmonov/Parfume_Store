from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models.users import User


class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "phone_number")

    @staticmethod
    def check_user_exists(phone):
        if User.objects.filter(phone_number=phone):
            raise ValidationError(f"User exist with phone number: {phone}")

    def validate(self, data):
        phone_number = data.get("phone_number")
        self.check_user_exists(phone_number)
        return data


class VerificationRegistrationCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    session = serializers.CharField()

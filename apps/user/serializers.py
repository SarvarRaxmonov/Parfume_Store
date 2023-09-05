from rest_framework import serializers
from apps.user.models.users import User
from rest_framework.exceptions import ValidationError


class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "phone_number"
        )

    @staticmethod
    def check_user_exists(phone):
        if User.objects.filter(phone_number=phone):
            raise ValidationError(f"User exist with phone number: {phone}")

    def validate(self, data):
        phone_number = data.get("phone_number")
        self.check_user_exists(phone_number)
        return data

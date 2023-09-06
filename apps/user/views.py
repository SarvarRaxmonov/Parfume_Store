import random
import string

from django.core import signing
from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.response import Response

from apps.user.cache import CacheTypes, generate_cache_key
from apps.user.models import User
from apps.user.serializers import (RecoveryCodeSerializer,
                                   RegisterUserSerializer, SendCodeSerializer,
                                   VerificationRegistrationCodeSerializer)
from apps.user.shared import send_verification_code


class SendCodeAPIView(generics.CreateAPIView):
    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]

        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
        send_verification_code(phone, CacheTypes.registration_sms_verification, session)
        return Response({"session": session})


class VerificationRegistrationCodeAPIView(generics.CreateAPIView):
    serializer_class = VerificationRegistrationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get("phone_number")
        code = serializer.validated_data.get("code")
        session = serializer.validated_data.get("session")

        cache_key = generate_cache_key(
            CacheTypes.registration_sms_verification, phone, session
        )

        if not self.is_code_valid(cache_key, code):
            return Response(
                {"detail": "Wrong code!"}, status=status.HTTP_400_BAD_REQUEST
            )

        signer = signing.TimestampSigner()
        phone_data = signer.sign_object(
            {"phone": phone, "type": CacheTypes.registration_sms_verification}
        )

        return Response({"phone": phone_data})

    @staticmethod
    def is_code_valid(cache_key, code):
        valid_code = cache.get(cache_key)
        if valid_code != code:
            return False
        return True


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class RecoveryCodeAPIView(generics.CreateAPIView):
    serializer_class = RecoveryCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]

        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
        send_verification_code(phone, CacheTypes.registration_sms_verification, session)
        return Response({"session": session})

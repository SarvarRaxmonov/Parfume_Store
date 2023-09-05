import random
import string

from apps.user.shared import send_verification_code
from rest_framework.views import APIView
from apps.user.serializers import SendCodeSerializer
from apps.user.cache import CacheTypes
from rest_framework.response import Response


class SendCodeAPIView(APIView):
    def post(self, request):
        serializer = SendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]

        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
        send_verification_code(phone, CacheTypes.registration_sms_verification, session)
        return Response({"session": session})

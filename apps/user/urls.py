from django.urls import path

from apps.user.views import (SendCodeAPIView,
                             VerificationRegistrationCodeAPIView)

urlpatterns = [
    path("send-code/", SendCodeAPIView.as_view(), name="send_code"),
    path("code-verify/", VerificationRegistrationCodeAPIView.as_view(), name="code_verify"),
]

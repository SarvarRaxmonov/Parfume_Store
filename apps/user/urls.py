from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.views import (
    RecoveryCodeAPIView,
    RegistrationAPIView,
    SendCodeAPIView,
    VerificationRegistrationCodeAPIView,
)


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("send-code/", SendCodeAPIView.as_view(), name="send_code"),
    path(
        "code-verify/",
        VerificationRegistrationCodeAPIView.as_view(),
        name="code_verify",
    ),
    path("registration/", RegistrationAPIView.as_view(), name="user_register"),
    path("send-recovery/", RecoveryCodeAPIView.as_view(), name="send_recovery"),
]

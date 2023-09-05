from django.urls import path
from apps.user.views import SendCodeAPIView

urlpatterns = [
    path("send-code/", SendCodeAPIView.as_view(), name="send_code")
]

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.user.models.notifications import Notification
from apps.user.models.users import User


class UserTest(APITestCase):
    def test_send_code(self):
        data = {"phone_number": "+998995004331"}
        result = self.client.post(reverse("send_code"), data)

        self.assertEqual(result.status_code, status.HTTP_200_OK)


class NotificationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password="test_password",
            phone_number="+998901234567",
            username="test_user",
        )
        self.notification = Notification.objects.create(
            title="Test Title",
            content="Test Content",
        )

    def test_all_notification(self):
        self.client.force_login(self.user)
        result = self.client.get(reverse("all_notifications"))
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_detail_notification(self):
        self.client.force_login(self.user)
        result = self.client.get(reverse("detail_notifications", kwargs={"pk": self.notification.id}))
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_read_user_notification(self):
        self.client.force_login(self.user)
        result = self.client.get(reverse("read_notifications"))
        self.assertEqual(result.status_code, status.HTTP_200_OK)

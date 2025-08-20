from django.test import TestCase, Client
from django.urls import reverse

from notifications.models import User


class NotificationApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            id=1,
            email="test@example.com",
            preferred_channels=["email"]
        )

    def test_send_notification_valid(self):
        data = {
            "user_id": 1,
            "title": "Привет",
            "message": "Тест"
        }
        response = self.client.post(
            reverse('send_notification'),
            data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()['user_id'], 1)

    def test_send_notification_invalid_user(self):
        data = {
            "user_id": 999,
            "title": "Привет",
            "message": "Тест"
        }
        response = self.client.post(
            reverse('send_notification'),
            data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("user_id", response.json())
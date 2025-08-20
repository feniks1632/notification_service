from django.test import TestCase
from unittest.mock import patch
from notifications.models import User, Notification
from notifications.services import NotificationService


class NotificationServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            preferred_channels=["email", "sms"]
        )
        self.service = NotificationService()

    @patch('notifications.providers.email.EmailProvider.send', return_value=True)
    def test_send_uses_first_successful_channel(self, mock_send):
        result = self.service.send_to_user(self.user, "Тест", "Сообщение")
        self.assertTrue(result)
        notification = Notification.objects.last()
        self.assertIn("email", notification.sent_chanels) # type: ignore
        self.assertEqual(notification.status, "sent") # type: ignore

    @patch('notifications.providers.email.EmailProvider.send', return_value=False)
    @patch('notifications.providers.sms.SMSProvider.send', return_value=True)
    def test_fallback_to_sms_if_email_fails(self, mock_sms, mock_email):
        result = self.service.send_to_user(self.user, "Тест", "Сообщение")
        self.assertTrue(result)
        mock_sms.assert_called_once()
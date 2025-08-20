from unittest.mock import patch
from django.test import TestCase
from celery.exceptions import Retry

from notifications.models import User
from notifications.tasks import send_notification_task


class TaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="test@example.com",
            preferred_channels=["email"]
        )

    @patch('notifications.providers.email.EmailProvider.send', return_value=True)
    def test_task_succeeds(self, mock_send):
        result = send_notification_task(1, "Тест", "Сообщение")
        self.assertIn("status", result)
        self.assertEqual(result["status"], "sent")

    @patch('notifications.providers.email.EmailProvider.send', return_value=False)
    @patch('notifications.providers.sms.SMSProvider.send', return_value=False)
    @patch('notifications.providers.telegram.TelegramProvider.send', return_value=False)
    def test_task_fails_all_channels(self, mock_tg, mock_sms, mock_email):
        # Задача должна выбросить Retry, потому что self.retry()
        with self.assertRaises(Retry):
            send_notification_task(1, "Тест", "Сообщение")
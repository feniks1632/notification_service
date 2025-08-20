from django.test import TestCase
from unittest.mock import patch, MagicMock

from notifications.models import User
from notifications.providers.email import EmailProvider
from notifications.providers.sms import SMSProvider
from notifications.providers.telegram import TelegramProvider


class ProvidersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            phone="79111234567",
            telegram_id="123456789"
        )

    @patch('notifications.providers.email.send_mail', return_value=1)
    def test_email_provider_sends(self, mock_send_mail):
        provider = EmailProvider()
        result = provider.send(self.user, "Тема", "Сообщение")
        self.assertTrue(result)
        mock_send_mail.assert_called_once()

    @patch('notifications.providers.sms.requests.post')
    def test_sms_provider_sends(self, mock_post):
        mock_post.return_value.json.return_value = {"success": True}
        provider = SMSProvider()
        result = provider.send(self.user, "Тема", "Сообщение")
        self.assertTrue(result)

    @patch('notifications.providers.telegram.requests.post')
    def test_telegram_provider_sends(self, mock_post):
        mock_post.return_value.json.return_value = {"ok": True}
        provider = TelegramProvider()
        result = provider.send(self.user, "Тема", "Сообщение")
        self.assertTrue(result)
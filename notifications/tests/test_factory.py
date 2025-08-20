from django.test import TestCase
from notifications.factory import NotificationProviderFactory


class ProviderFactoryTest(TestCase):
    def test_get_email_provider(self):
        provider = NotificationProviderFactory.get_provider('email')
        self.assertEqual(provider.__class__.__name__, 'EmailProvider')

    def test_get_sms_provider(self):
        provider = NotificationProviderFactory.get_provider('sms')
        self.assertEqual(provider.__class__.__name__, 'SMSProvider')

    def test_get_telegram_provider(self):
        provider = NotificationProviderFactory.get_provider('telegram')
        self.assertEqual(provider.__class__.__name__, 'TelegramProvider')

    def test_invalid_channel_raises_value_error(self):
        with self.assertRaises(ValueError):
            NotificationProviderFactory.get_provider('invalid_channel')            
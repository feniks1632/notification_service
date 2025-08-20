from django.test import TestCase

from notifications.models import User, Notification


class UserModel(TestCase):
    def test_str_returns_or_id(self):
        user = User.objects.create(email="test@example.com")
        user_no_email = User.objects.create(phone="79111234567")
        user_no_contact = User.objects.create()
        self.assertEqual(str(user), "test@example.com")
        self.assertEqual(str(user_no_email), "79111234567")
        self.assertEqual(str(user_no_contact), f"User {user_no_contact.id}") # type: ignore
            
class NotificationModel(TestCase):
    def test_str_contains_title_and_user(self):
        user = User.objects.create(email="test@example.com")
        notification = Notification.objects.create(
            user=user,
            title="Привет",
            message="Тест"
        )
        self.assertIn("Привет", str(notification))
        self.assertIn("test@example.com", str(notification))
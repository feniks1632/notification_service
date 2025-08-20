import logging

from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger(__name__)

class EmailProvider:
    """
    Для отправки email
    """

    def send(self, user, title, message):
        if not user.email:
            return False
        
        try:
            send_mail(
                subject=title,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False
            )
            return True
        except Exception as e:
            logger.info(f"[EmailProvider] Ошибка отправки на {user.email}: {e}")
            return False
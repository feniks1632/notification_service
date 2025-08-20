import logging

from .factory import NotificationProviderFactory
from .models import Notification

logger = logging.getLogger(__name__)


class NotificationService:
    """
    Сервис отправки уведомлений с fall-back логикой.
    Использует фабрику для получения провайдера
    """

    def send_to_user(self, user, title, message):
        notification = Notification.objects.create(
            user=user,
            title=title,
            message=message
        )

        # Приоритет каналов
        channels = user.preferred_channels or NotificationProviderFactory.get_aviable_chanels() 
        
        for channel in channels:
            try:
                provider = NotificationProviderFactory.get_provider(channel)
                if provider.send(user,title, message):
                    notification.sent_chanels.append(channel)
                    notification.status = 'sent'
                    notification.save()
                    return True
            except Exception as e:
                logger.error(f"[NotificationService] Ошибка при отправке через {channel}: {e}")

        # Если каналы не прошли
        notification.status = 'failed'
        notification.save()
        return False

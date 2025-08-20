import logging

from celery import shared_task
from .models import User
from .services import NotificationService

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_notification_task(self, user_id: int, title: str, message: str):
    """
    Асинхронная задача по отправке уведомления.
    При неудаче повторяет попытку до трех раз.
    """
    try:
        user = User.objects.get(id=user_id)
        service = NotificationService()
        success = service.send_to_user(user, title, message)

        if not success:
            raise Exception("Все каналы доставки не сработали")
        
        return {'status': 'sent', 'user_id': user_id}
    
    except Exception as exc:
        # Логируем и пробуем повторить
        logger.error(f"[send_notification_task] Ошибка: {exc}")
        self.retry(ex=str(exc), countdown=60)

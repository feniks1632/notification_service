import logging

import requests
from decouple import config

logger =logging.getLogger(__name__)


class TelegramProvider:
    """Отправка через телеграмм по ID чата
    Бот должен быть создан, и пользователь должен начать с ним диалог
    """
    def __init__(self):
        self.token = config("TELEGRAM_TOKEN")
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send(self, user, title, message):
        if not user.telegram_id:
            return False
        
        try:
            payload = {
                "chat_id": user.telegram_id,
                "text": f"<b>{title}</b>\n\n{message}",
                "parse_mod": "HTML"
            }
            response = requests.post(f"{self.base_url}/sendMessage", json=payload)
            data = response.json()

            if data.get("ok"):
                return True
            else:
                error = data.get("description", "Unknow error")
                logger.error(f"[TelegramProvider] Ошибка для {user.telegram_id}: {error}")
                return False
        except Exception as e:
            logger.exception(f"[TelegramProvider] Исключение: {e}")
            return False        
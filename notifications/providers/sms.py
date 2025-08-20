import logging

import requests
from decouple import config

logger =logging.getLogger(__name__)

class SMSProvider:
    """
    Отправка sms через sms.ru
    """

    API_URL = "https://sms.ru/sms/send"

    def send(self, user, title, message):
        if not user.phone:
            return False
        
        try:
            params = {
                "api_id": config("SMS_API_KEY"),
                "to": user.phone,
                "msg": f"{title}\n{message}",
                "json": 1
            }
            response = requests.post(self.API_URL, data=params)
            data = response.json()

            #100 - успех
            if data.get("status") == "OK" and data["status_code"] == 100:
                return True
            else:
                logger.info(f"[SMSProvider] Ошибка {data.get('status_text')}")
                return False
        except Exception as e:
            logger.info(f"[SMSProvider] Исключение при отправке на {user.phone}: {e}")
            return False    
        

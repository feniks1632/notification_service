import logging
import json

import requests
from decouple import config

logger =logging.getLogger(__name__)

class SMSProvider:
    API_URL = "https://gate.smsaero.ru/v2/sms/send"

    def send(self, user, title, message):
        if not user.phone:
            logger.info("[SMSProvider] Нет номера телефона")
            return False

        try:
            # Форматируем номер
            phone_str = user.phone.strip().lstrip('+').lstrip('8')
            if not phone_str.startswith('7'):
                phone_str = '7' + phone_str.lstrip('7')
            try:
                phone = int(phone_str)
            except ValueError:
                logger.error(f"[SMSProvider] Неверный формат номера: {user.phone}")
                return False

            payload = {
                "number": phone,
                "text": f"{title}\n{message}",
                "sign": "SMS Aero"
            }

            auth = (config('SMSAERO_LOGIN'), config('SMSAERO_API_KEY'))
            
            headers = {
                "Content-Type": "application/json"
            }

            # Логируем, что отправляем
            logger.info(f"[SMSProvider] Отправка SMS: {payload}")

            response = requests.post(
                self.API_URL,
                data=json.dumps(payload),
                headers=headers,
                auth=auth # type: ignore
            )

            logger.info(f"[SMSProvider] HTTP {response.status_code}")
            logger.info(f"[SMSProvider] Response body: {response.text}")

            if response.status_code == 200:
                data = response.json()
                if data.get("success") is True:
                    logger.info("[SMSProvider] SMS отправлена успешно")
                    return True
                else:
                    error = data.get("error", "Unknown error")
                    logger.error(f"[SMSProvider] SmsAero error: {error}")
                    return False
            else:
                logger.info(f"[SMSProvider] HTTP ошибка: {response.status_code} — {response.text}")
                return False

        except Exception as e:
            logger.info(f"[SMSProvider] Исключение: {e}")
            return False
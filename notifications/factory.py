from .providers.email import EmailProvider
from .providers.sms import SMSProvider
from .providers.telegram import TelegramProvider


class NotificationProviderFactory:
    """
    Фабрика для создания провайдеров уведомлений по ключу
    """

    _providers = {
        "email": EmailProvider,
        "sms": SMSProvider,
        "telegram": TelegramProvider
    }

    @classmethod
    def get_provider(cls, channel):
        """
        Возвращаем провайдер по имени канала
        """
        if channel not in cls._providers:
            raise ValueError(f"Неизвестный канал уведомлений {channel}")
        
        return cls._providers[channel]()
    
    @classmethod
    def get_aviable_chanels(cls):
        """
        Возвращает список доступных каналов
        """
        return list(cls._providers.keys())

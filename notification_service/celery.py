from __future__ import absolute_import, unicode_literals
import logging
import os

from celery import Celery
from django.conf import settings

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_service.settings')

app = Celery('notification_service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


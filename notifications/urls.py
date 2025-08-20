from django.urls import path

from . import views


urlpatterns = [
    path('api/notify', views.SendNotificationView.as_view(), name='send_notification'),
]
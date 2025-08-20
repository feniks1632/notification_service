from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SendNotificationSerializer
from .tasks import send_notification_task


@extend_schema(
    description="Отправляет уведомление пользователю. Использует fallback-логику: Telegram → Email → SMS.",
    examples=[
        OpenApiExample(
            name="Успешный запрос",
            summary="Пример отправки уведомления",
            description="Отправка уведомления пользователю с ID 1",
            value={
                "user_id": 1,
                "title": "Новое уведомление",
                "message": "Вы получили новое сообщение!"
            },
            request_only=True,  # Только для запроса
            response_only=False,
        ),
        OpenApiExample(
            name="Ошибка валидации",
            summary="Неверный user_id",
            description="Если user_id не существует",
            value={
                "user_id": ["Пользователь с таким ID не найден."]
            },
            request_only=False,
            response_only=True,  # Только для ответа
        )
    ]
)

class SendNotificationView(APIView):
    serializer_class = SendNotificationSerializer
    def post(self, request):
        serializer = SendNotificationSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id'] # type: ignore
            title = serializer.validated_data['title'] # type: ignore
            message = serializer.validated_data['message'] # type: ignore

            send_notification_task.delay(user_id, title, message) # type: ignore

            return Response(
                {"status": "queued", "user_id": user_id},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
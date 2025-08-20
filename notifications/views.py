from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SendNotificationSerializer
from .tasks import send_notification_task


class SendNotificationView(APIView):
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
    
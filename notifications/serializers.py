from rest_framework import serializers
from .models import User


class SendNotificationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    message = serializers.CharField()


    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("Пользователь с таким ID не найден")
        return value
from django.contrib import admin

from .models import User, Notification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'telegram_id')
    search_fields = ('email', 'phone')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    search_fields = ('status', 'created_at' )
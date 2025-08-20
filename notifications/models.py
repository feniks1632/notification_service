from django.db import models

class User(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    telegram_id = models.CharField(max_length=50, blank=True, null=True)
    prefered_chanels = models.JSONField(
        default=list, 
        help_text="Приоритет каналов: ['telegram', 'email', 'sms']"
    )

    def __str__(self):
        return self.email or self.phone or f" User {self.id}"
    
    class Meta:
        db_table = "notification_user"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    sent_chanels = models.JSONField(default=list) # email
    status = models.CharField(max_length=20 ,default='pending') # pending, sent, failed
    created_at = models.DateTimeField(auto_now_add=True)
    retry_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.title} -> {self.user}"
    
    class Meta:
        db_table = "notification"
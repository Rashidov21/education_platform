from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s {self.plan.capitalize()} Subscription"

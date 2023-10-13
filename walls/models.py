from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Wall(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, default=1)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s Wall Post"

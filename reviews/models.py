from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #<- , null=True

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s review"
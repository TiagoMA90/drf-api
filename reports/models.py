from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Report(models.Model):
    REASON_CHOICES = [
        ('spam', 'Spam'),
        ('inappropriate', 'Inappropriate Content'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100, choices=REASON_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} reported {self.post.title}'

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

REPORT_CHOICES = [
    ('spam_flame', 'Spamming and Flaming'),
    ('inappropriate', 'Inappropriate Content'),
    ('other', 'Other'),
]

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.CharField(max_length=32, choices=REPORT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.reporter.username} reported '{self.post.title}' for {self.get_reason_display()}"

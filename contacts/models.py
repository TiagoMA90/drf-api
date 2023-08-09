from django.db import models

# Contact us Model
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
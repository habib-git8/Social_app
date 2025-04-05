from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='static/images', blank=True, null=True)  # Store images
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    def __str__(self):
        return self.title
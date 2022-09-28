from email.mime import image
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=255)
    category = models.DateField(max_length=255)
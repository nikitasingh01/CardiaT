
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Idea(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comments(models.Model):
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    idea=models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments')

# Create your models here.


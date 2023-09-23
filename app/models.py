from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):

    first_name= models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Event(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_events')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_events')

    def __str__(self):
        return self.title


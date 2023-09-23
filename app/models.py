from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    first_name= models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

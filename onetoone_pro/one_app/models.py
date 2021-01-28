from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=70)

    def __str__(self):
        return self.user.username

from django.db import models


# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)

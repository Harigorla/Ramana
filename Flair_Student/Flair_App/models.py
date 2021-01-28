from django.db import models
from django.contrib.auth.models import User


class FlairInstitute(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=70)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    ssc = models.IntegerField()
    inter = models.IntegerField()
    profile_pic = models.ImageField(upload_to='image/')
    loc = models.CharField(max_length=50)


class Flair(models.Model):
    institute = models.OneToOneField(User, on_delete=models.CASCADE)

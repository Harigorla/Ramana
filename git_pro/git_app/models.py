from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=70)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    ssc = models.IntegerField(null=True)
    inter = models.IntegerField(null=True)
    address = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def is_selected(self):
        return 850 >= self.inter

    def __str__(self):
        return self.user.username

    def __str__(self):
        today = date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)

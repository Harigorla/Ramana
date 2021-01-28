from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=70)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=80)

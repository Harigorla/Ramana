from django.db import models


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=80)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)
   
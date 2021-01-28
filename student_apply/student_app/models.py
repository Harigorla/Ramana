from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200, primary_key=True)
    phone = models.IntegerField(unique=True)
    ssc = models.CharField(max_length=100)
    inter = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='images')
    currentaddress = models.CharField(max_length=1000)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=30)
    positionapply = models.CharField(max_length=300)
    isactive = models.BooleanField(default=False)


class Staff(models.Model):
    pass

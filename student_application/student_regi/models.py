from django.db import models


class Student(models.Model):
    firstname = models.CharField(verbose_name='First Name', max_length=100)
    lastname = models.CharField(verbose_name='Last Name', max_length=200)
    username = models.CharField(verbose_name='User Name', max_length=200, primary_key=True)
    email = models.EmailField(verbose_name='Email Field', max_length=200)
    dob = models.DateField(verbose_name='Date Of Birth')
    password = models.CharField(max_length=20)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    image = models.ImageField(upload_to='image/')
    ssc = models.IntegerField(verbose_name='SSC Marks')
    inter = models.IntegerField(verbose_name='Inter Marks')
    DEPT_CHOICES = [
        ('H', 'Hr'),
        ('M', 'Marketing'),
        ('F', 'Finance'),
        ('C', 'Cat'),
    ]
    department = models.CharField(choices=DEPT_CHOICES, max_length=2)
    is_selected = models.BooleanField(default=True)

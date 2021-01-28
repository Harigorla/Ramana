from django.db import models
from django.contrib.auth.models import User


class StudentApplication(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    ssc = models.IntegerField()
    inter = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def is_selected(self):
        return self.inter >= 750


class StudentRegistration(models.Model):
    student_application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)
    ssc = models.IntegerField()
    inter = models.IntegerField()


class StaffRegistration(models.Model):
    staff_user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass


class StaffDepartment(models.Model):
    staff_registration = models.ForeignKey(StaffRegistration, on_delete=models.CASCADE)
    pass

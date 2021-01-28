from .models import Student, Staff
from django.forms import ModelForm


class StudentApplicationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','email', 'ssc', 'inter', 'birthdate','phone', 'pincode', 'city','currentaddress']


class StudenyRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'password', 'email', 'pic', 'ssc', 'inter', 'birthdate']


class StudentLoginForm(ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password']
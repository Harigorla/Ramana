from django.forms import ModelForm
from .models import Student


class StudentApplicationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email', 'dob', 'gender', 'ssc', 'inter']


class StudentRegisterForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'username','password' ,'email', 'dob', 'department', 'is_selected', 'image', 'ssc', 'inter']


class StudentLoginForm(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']
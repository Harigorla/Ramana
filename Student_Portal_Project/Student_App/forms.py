from django.forms import ModelForm
from .models import StudentApplication


class StudentApplicationForm(ModelForm):
    class Meta:
        model = StudentApplication
        fields = "__all__"
        #fields = ['firstname', 'lastname', 'dob', 'gender', 'ssc', 'inter', 'is_verified']


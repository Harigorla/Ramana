from django import forms
from django.contrib.auth.models import User
from .models import FlairInstitute, Flair


class FlairForm(forms.ModelForm):
    class Meta():
        model = Flair
        fields = ['username', 'email', 'password']


class FlairInstituteForm(forms.ModelForm):
    loc = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = FlairInstitute
        fields = ['firstname', 'lastname', 'gender', 'ssc', 'inter', 'profile_pic', 'loc']

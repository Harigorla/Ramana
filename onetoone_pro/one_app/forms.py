from django import forms
from .models import UserProfile, User
from django.contrib.auth.forms import UserCreationForm


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=80)
    lastname = forms.CharField(max_length=70)

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']

        if commit:
            user.save()
        return User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'location']

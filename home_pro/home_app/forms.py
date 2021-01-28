from django.forms import ModelForm
from .models import Registration


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"


class LoginForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['user_name', 'password']

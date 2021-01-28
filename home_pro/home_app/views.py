from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Registration
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def home_page(request):
    return render(request, 'home.html')


def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
            return redirect('/log_in')
    else:
        rform = RegistrationForm()
        return render(request, 'registration.html', {'rform': rform})


def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            user_name = request.POST.get('user_name', '')
            password = request.POST.get('password', '')
            user = Registration.objects.filter(
                user_name=user_name
            )
            pwd = Registration.objects.filter(
                password=password
            )
            if user and pwd:
                return redirect('/log_out')
            else:
                return HttpResponse('Invalid Details')
    else:
        lform = LoginForm()
        return render(request, 'log_in.html', {'lform': lform})


def log_out_view(request):
    auth_logout(request)
    return redirect('/home_page')

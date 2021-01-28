from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse
from .models import UserProfile
from .forms import ExtendedUserCreationForm, UserProfileForm


def home(request):
    data = UserProfile.objects.all()
    return render(request, 'home.html', {'data': data})


def register_view(request):
    if request.method == "POST":
        rform = ExtendedUserCreationForm(request.POST)
        pform = UserProfileForm(request.POST)
        if rform.is_valid() and pform.is_valid():
            user = rform.save()
            user.save()
            prifile = pform.save(commit=False)
            profile.user = user
            prifile.save()
            return HttpResponse('saved')

        return HttpResponse('Save')
    else:
        rform = ExtendedUserCreationForm()
        pform = UserProfileForm()
    return render(request, 'register.html', {'rform': rform, 'pform': pform})

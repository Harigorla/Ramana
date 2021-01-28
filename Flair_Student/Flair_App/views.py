from django.shortcuts import render
from .forms import FlairForm, FlairInstituteForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register_view(request):
    if request.method == "POST":
        fform = FlairForm(data=request.POST)
        fiform = FlairInstituteForm(data=request.POST)
        if fform.is_valid() and fiform.is_valid():
            user = fform.save()
            user.set_password(user.password)
            user.save()
            fi = fiform.save(commit=False)
            fi.user = user
            if 'profile_pic' in request.FILES:
                print('Found it')
                fi.profile_pic = request.FILES['profile_pic']
            fi.save()
        else:
            print(fform.errors, fiform.errors)
    else:
        fform = FlairForm()
        fiform = FlairInstituteForm()
        return render(request, 'registration.html', {'fform': fform, 'fiform': fiform})










from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentApplication
from .forms import StudentApplicationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'Home.html')


def student_apply_view(request):
    if request.method == "POST":
        sform = StudentApplicationForm(data=request.POST)
        if sform.is_valid():
            sform.save()
            return HttpResponse('save')
        return HttpResponse('Not Save')
    else:
        sform = StudentApplicationForm()
    return render(request, 'student_apply.html', {'sform': sform})

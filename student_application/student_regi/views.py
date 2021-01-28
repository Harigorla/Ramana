from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from .forms import StudentApplicationForm, StudentRegisterForm, StudentLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def student_apply_view(request):
    if request.method == "POST":
        sform = StudentApplicationForm(request.POST, request.FILES)
        if sform.is_valid():
            sform.save()
            return redirect('/studentregistration')
    else:
        sform = StudentApplicationForm()
    return render(request, 'studentapply.html', {'sform': sform})


def student_register_view(request):
    if request.method == "POST":
        rform = StudentRegisterForm(request.POST)
        if rform.is_valid():
            rform.save()

            return redirect('/studentlogin')
    else:
        rform = StudentRegisterForm()
    return render(request, 'studentregister.html', {'rform': rform})


def student_login_view(request):
    if request.method == "POST":
        lform = StudentLoginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username', ' ')
            password = request.POST.get('password', ' ')
            user = Student.objects.filter(username=username)
            pwd = Student.objects.filter(password=password)
            if user and pwd:
                return HttpResponse('valid')
            else:
                return HttpResponse('invalid')
    else:
        lform = StudentLoginForm()
    return render(request, 'login.html', {'lform': lform})
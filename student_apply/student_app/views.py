from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, Staff
from .forms import StudentApplicationForm, StudenyRegistrationForm, StudentLoginForm


def home(request):
    return render(request, 'home.html')


def student_aview(request):
    if request.method == "POST":
        aform = StudentApplicationForm(request.POST, request.FILES)
        if aform.is_valid():
            aform.save()
            return redirect('/studentregistration')
    else:
        aform = StudentApplicationForm()
    return render(request, 'studentapply.html', {'aform': aform})


def student_rview(request):
    if request.method == "POST":
        rform = StudenyRegistrationForm(request.POST, request.FILES)
        if rform.is_valid():
            rform.save()
            return redirect('/studentlogin')
    else:
        rform = StudenyRegistrationForm()
    return render(request, 'studentregister.html', {'rform': rform})


def student_lview(request):
    if request.method == "POST":
        lform = StudentLoginForm(request.POST, request.FILES)
        if lform.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            ema = Student.objects.filter(email=email)
            pwd = Student.objects.filter(password=password)
            if ema and pwd:
                return redirect('/detail')
            else:
                return HttpResponse('invaild details')
    else:
        lform = StudentLoginForm()
    return render(request, 'studentlogin.html', {'lform': lform})


def detail(request):
    student = Student.objects.all()
    return render(request, 'detail.html', {'student_list': student})


def staff_aview(request):
    pass


def staff_lview(request):
    pass

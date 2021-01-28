from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def create_view(request):
    if request.method == "POST":
        cform = RecipeForm(request.POST, request.FILES)
        if cform.is_valid():
            cform.save()
            return HttpResponse('Save')
    else:
        cform = RecipeForm()
        return render(request, 'create.html', {'cform': cform})


def detail(request, recipe_id):
    items = Recipe.objects.get(id=recipe_id)
    return render(request, 'detail.html', {'items': items})


@login_required
def index(request):
    return render(request, 'accounts/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'sign_up.html', context)

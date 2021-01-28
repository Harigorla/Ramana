from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import RecipeCreateForm
from .models import Recipe

def recipe_create(request):
    if request.POST:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            redirect('detail')
    else:
        form = RecipeCreateForm()
        return render(request, 'xyz.html', {'form': form})


def detail(request):
    data = get_object_or_404(Recipe)
    return render(request, 'detail.html', {'data': data})
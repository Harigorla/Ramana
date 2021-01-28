from django.shortcuts import render
from django.http import HttpResponse


def geeks_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")


def home(request):
    data = {"name": "Hari",
            "age": 25,
            "location": "Bangalore",
            "education": [{"type": "Ssc", "location": "Kadapa", "name": "Harinadha", "marks": 518},
                          {"type": "Inter", "location": "AP", "name": "Cec", "marks": 941},
                          {"type": "Mba", "location": "Jntu", "name": "Reddy", "marks": 71.1}]}
    return render(request, "hari.html", data)


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

from django.contrib import admin
from django.urls import path
from login_app import views

urlpatterns = [
    path("", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]
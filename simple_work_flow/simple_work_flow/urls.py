from django.contrib import admin
from django.urls import path
from simple_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.geeks_view),
    path('home/',views.home),
    path('home1/', views.index),
]

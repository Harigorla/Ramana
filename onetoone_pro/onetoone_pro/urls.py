from django.contrib import admin
from django.urls import path
from one_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register_view, name='register'),
    path('', views.home, name='home'),
]

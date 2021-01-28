from django.contrib import admin
from django.urls import path

from git_app import views

app_name = 'git_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('special/', views.special, name='special'),
    path('apply/', views.apply_view, name='apply'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]

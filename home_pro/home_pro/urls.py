from django.contrib import admin
from django.urls import path
from home_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/', views.home_page, name='home_page'),
    path('registration/', views.registration_view, name='registration'),
    path('log_in/', views.login_view, name='log_in'),
    path('log_out/', views.log_out_view, name='log_out')
]

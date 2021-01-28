from django.contrib import admin
from django.urls import path
from recipenewapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.recipe_create),
    path('detail/', views.detail),
]

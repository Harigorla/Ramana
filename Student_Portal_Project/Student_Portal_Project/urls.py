from django.contrib import admin
from django.urls import path
from Student_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('studentapply/', views.student_apply_view, name='studentapply'),

]

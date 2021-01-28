from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student_regi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('studentapplication/', views.student_apply_view, name='application'),
    path('studentregistration/', views.student_register_view, name='registration'),
    path('studentlogin/', views.student_login_view, name='studentlogin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

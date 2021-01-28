from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student_app import views

app_name = "student_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('studentapplication/', views.student_aview, name='studentapplication'),
    path('studentregistration/', views.student_rview, name='studentregistration'),
    path('studentlogin/', views.student_lview, name='studentlogin'),
    path('detail/', views.detail, name='detail'),
    path('staffregistration/', views.staff_aview, name='staffregistration'),
    path('stafflogin/', views.staff_lview, name='stafflogin')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

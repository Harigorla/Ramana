from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from serial_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('hello/', views.HelloView.as_view(),name='hello'),
]

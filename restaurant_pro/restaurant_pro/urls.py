from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from restaurant_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_view),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

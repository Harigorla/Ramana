from django.contrib import admin
from django.urls import path
from votes_app import views

app_name = 'votes_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<int:question_id>/',views.detail, name='deatil'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

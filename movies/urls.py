from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    
    path('<int:id>/scores/new/', views.scores_new, name='scores_new'),
    path('<int:id>/scores/<int:score_id>/delete', views.score_delete, name='score_delete'),
]

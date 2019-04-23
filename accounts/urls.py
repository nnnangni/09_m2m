from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.user_page, name='user_page'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('follow/<int:id>', views.follow, name='follow'),
    path('<int:id>/followers/', views.followers, name='followers'),
    path('<int:id>/followings/', views.followings, name='followings'),
]
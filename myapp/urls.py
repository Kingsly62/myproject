from myapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.register_view, name='register'),
    path('gallerly/', views.gallery, name='gallerly'),
    path('project', views.project, name='project'),
    path('home', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    
    path('welcome', views.welcome, name='welcome'),
    
    
    
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),

]

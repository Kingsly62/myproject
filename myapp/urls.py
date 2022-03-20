from myapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.project, name='project'),
    path('register/', views.register_view, name='register'),
    path('gallerly/', views.gallery, name='gallerly'),
    
    path('home', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    
    path('welcome', views.welcome, name='welcome'),
    
    
    
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),

]


# heroku pg:push project DATABASE_URL --app clinton-project

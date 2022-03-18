from myapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.project, name='project'),
    path('home', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('welcome', views.welcome, name='welcome')
]

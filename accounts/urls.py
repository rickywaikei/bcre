from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),   # End points: 'register' used by url, name='register' used by templates
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]

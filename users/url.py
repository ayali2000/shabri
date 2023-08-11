from django import views
from django.urls import path
from . views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'general/index.html'),name='logout')
]
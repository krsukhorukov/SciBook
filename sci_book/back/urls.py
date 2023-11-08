from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404
from django.conf.urls import handler500

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', Main.as_view(), name='main'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
    path('registration/', views.RegisterUserView.as_view(), name='registration'),
    #path('profile/', views.ProfileView.as_view(), name='profile'),
]

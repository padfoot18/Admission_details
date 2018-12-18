from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='home'),
    path('signup/', views.UserSignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
]
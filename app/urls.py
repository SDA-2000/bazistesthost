from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.red),
    path('accounts/login/', views.login, name='login'),
    path('accounts/registration', views.registration, name='reg'),
    path('accounts/profile/<str:username>/', views.profile, name='profile'),
]

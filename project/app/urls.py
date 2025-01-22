from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.red),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/change/<str:change_user>/', views.change_user_data, name='change_user_data'),
    path('profile/<str:username>/delete/<str:del_user>/', views.delete_user, name='delete_user'),
    path('profile/<str:username>/add', views.add_user, name='add'),
]

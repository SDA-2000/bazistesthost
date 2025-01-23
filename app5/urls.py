from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_endp, name = 'guest'),
    path('me', views.get2_endp_crud_read),
    path('accounts/login/', views.login, name='login'),
    path('accounts/registration', views.registration),
    path('accounts/profile/<str:username>/', views.get2_endp_crud_read, name='profile'),
    path('accounts/profile/<str:username>/change/<str:change_user>/', views.change_user_data, name='change_user_data'),
    path('accounts/profile/<str:username>/delete/<str:del_user>/', views.delete_user, name='delete_user')
]

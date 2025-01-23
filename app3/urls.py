from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.red),
    path('endp/', views.endp, name='endp'),
    path('endp/post', views.post, name='post'),
]
